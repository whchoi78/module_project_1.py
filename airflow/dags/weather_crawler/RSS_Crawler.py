from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta, date
from exceptions import *
import pymysql
import requests
import urllib.request as ur

class WeatherCrawler(object):
    def __init__ (self, write_handler=None):
        self.url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
        self.datetime = datetime.today()
        self.weather_data = []
        self.write_handler = write_handler

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
        print('crawling start')
        request = self.connect_url(self.url)
        documents = bs(request.content, "html.parser").find_all('location')
        for document in documents:
            datas = document.find_all('data')
            for data in datas:
                self.write_handler((data.tmef.string, document.city.string, data.tmx.string, data.tmn.string, data.wf.string, data.rnst.string))
                documents_data = {}
                documents_data['weather_time'] = data.tmef.string # 날짜 + 기준시각
                documents_data['dist'] = document.city.string # 지역 이름
                documents_data['temp_max'] = data.tmx.string # 최고온도
                documents_data['temp_min'] = data.tmn.string # 최저온도
                documents_data['weather_sky'] = data.wf.string # 날씨
                documents_data['rnst'] = data.rnst.string # 강수 확률
                self.weather_data.append(documents_data)
        
        # for dline in self.weather_data:
        #     print(str(dline))
        # return self.weather_data
        
    def start(self):
        print('weather_crawler start')
        return self.get_data()
        

if __name__ == "__main__":
    Crawler = WeatherCrawler()
    Crawler.start()