from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta, date
import exceptions
import pymysql
import requests
import urllib.request as ur

class WeatherCrawler(object):
    def __init__ (self, datetime = date.today(), write_handler=None):
        if not len(str(code_num)) == 10:
            InvalidCodenumber()
        self.url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone='
        
        self.datetime = datetime
        self.weather_data = []
        self.write_handler = write_handler

        self.conn =  pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="p@ssw0rd", 
            charset="utf8", 
        )
        self.curs = self.conn.cursor()

    def get_target_code(self):
        #target_url = list(self.curs.execute("SELECT code FROM "))
        target_url = [1111061500, 1121583000]
        return target_url

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
        target_codes = self.get_target_code()
        for code in target_codes:
            request = self.connect_url(self.url+str(code))
            documents = bs(request.content, "html.parser").find_all('data')
            for data in documents:
                documents_data = {}
                documents_data['weather_time'] = str((self.datetime+timedelta(days=int(data.day.string))).strftime('%Y%m%d'))+data.hour.string # 날짜 + 기준시각
                documents_data['code'] = code # 동네 코드
                documents_data['temp_max'] = data.tmx.string # 최고온도
                documents_data['temp_min'] = data.tmn.string # 최저온도
                documents_data['weather_sky'] = data.wfkor.string # 날씨
                documents_data['wind_speed'] = data.ws.string # 풍속
                documents_data['wind_direction'] = data.wdkor.string # 풍향
                documents_data['pop'] = data.pop.string # 강수 확률
                self.weather_data.append(documents_data)
        print(self.weather_data)
    def start(self):
        get_data(self)

if __name__ == "__main__":
    Crawler = WeatherCrawler()
    Crawler.get_data()