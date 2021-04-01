from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta, date
#import exceptions
import requests
import json
import pymysql
import urllib.request as ur

#================================================테이블 생성, 및 초기값 작성=====================================================================

def create_tables():
    with pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="p@ssw0rd", 
        charset="utf8", 
        database="mydb"
    ) as connection:
        with connection.cursor() as cursor:
            create_code_table_query = """
                CREATE TABLE IF NOT EXISTS code_table (
                                loc_code int, root_loc varchar(45),
                                /*middle_loc varchar(100), end_loc varchar(100)*/
                                PRIMARY KEY (loc_code)
                );
            """

            create_middle_weather_table_query = """
            CREATE TABLE IF NOT EXISTS mw_table (
                            weather_time varchar(200),
                            dist varchar(45),
                            temp_max varchar(45),
                            temp_min varchar(45),
                            weather_sky varchar(45),
                            rnst varchar(45),
                            PRIMARY KEY (weather_time, dist)
                );
            """

            cursor.execute(create_code_table_query)
            cursor.execute(create_middle_weather_table_query)
            
            connection.commit()

            print("테이블 생성 완료")
    return

def insert_code_table():
    url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
    codeloc_arr = []
    #print(url)
    req = requests.get(url)
    req.encoding = 'utf-8'
    rDict = json.loads(req.text)
    for test in rDict:
        codeloc_arr.append((int(test.get('code')),test.get('value')))

    #print(codeloc_arr)

    with pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="p@ssw0rd", 
        charset="utf8", 
        database="mydb"
    ) as connection:
        with connection.cursor() as cursor:

            delete_code_table_query = "truncate table code_table;"

            insert_code_table_query = """
            insert into code_table (loc_code, root_loc) values(%s, %s)
            """
            cursor.execute(delete_code_table_query)
            cursor.executemany(insert_code_table_query, codeloc_arr)
 
            connection.commit()

            print("코드 테이블 업데이트 완료")
    
    return 

create_tables() # --> 테이블 첫 생성
insert_code_table() #--> 첫 크롤링

#==================================================크롤링=====================================================================

class WeatherCrawler(object):
    def __init__ (self, datetime = date.today(), write_handler=None):
        self.url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
        self.datetime = datetime
        self.weather_data = []
        self.write_handler = write_handler

        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="p@ssw0rd", 
            charset="utf8", 
        )
        self.curs = self.conn.cursor()

    @staticmethod
    def connect_url(url, max_tries=5):
        remaining_tries = int(max_tries)
        while remaining_tries > 0:
            try:
                return requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            except requests.exceptions:
                sleep(1)
            remaining_tries = remaining_tries - 1
        raise ResponseTimeout()
    
    def get_data(self):
        request = self.connect_url(self.url)
        documents = bs(request.content, "html.parser").find_all('location')

        wt_list = []
        code_list = []
        di_list = []
        temx_list = []
        temi_list = []
        wesk_list = []
        rn_list = []

        for document in documents:
            datas = document.find_all('data')
            for data in datas:
                documents_data = {}
                documents_data['weather_time'] = data.tmef.string # 날짜 + 기준시각
                documents_data['dist'] = document.city.string # 지역 이름
                documents_data['temp_max'] = data.tmx.string # 최고온도
                documents_data['temp_min'] = data.tmn.string # 최저온도
                documents_data['weather_sky'] = data.wf.string # 날씨
                documents_data['rnst'] = data.rnst.string # 강수 확률
                self.weather_data.append(documents_data)

                wt_list.append(str(documents_data['weather_time']).replace('-','').replace(':','').replace(' ','').strip())
                di_list.append(str(documents_data['dist']))
                temx_list.append(str(documents_data['temp_max']))
                temi_list.append(str(documents_data['temp_min']))
                wesk_list.append(str(documents_data['weather_sky']))
                rn_list.append(str(documents_data['rnst']))

        all_data_list = []
        for x in range(0,len(wt_list)-1,1):
            all_data_list.append((wt_list[x],di_list[x],temx_list[x],temi_list[x],wesk_list[x],rn_list[x]))
                
        with pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="p@ssw0rd", 
            charset="utf8", 
            database="mydb"
        ) as connection:
            with connection.cursor() as cursor:
                delete_mw_table_query = "truncate table mw_table;"

                insert_mw_table_query = """
                insert into mw_table (
                weather_time, dist,
                temp_max, temp_min,
                weather_sky, rnst) 
                values (%s, %s, %s, %s, %s, %s)
                """

                cursor.execute(delete_mw_table_query)
                cursor.executemany(insert_mw_table_query, all_data_list)
    
                connection.commit()

                print("크롤링 완료")

    
        
    def start(self):
        return self.get_data()
        

if __name__ == "__main__":
    Crawler = WeatherCrawler()
    Crawler.start()
