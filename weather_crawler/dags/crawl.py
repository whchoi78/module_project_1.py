from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from weather_crawler.mysql import MySQLDB
from weather_crawler.RSS_Crawler import WeatherCrawler
import os

def crawl():
    mysql = MySQLDB(
        host = "test_mysql_1",
        port = 3306,
        user = "airflow",
        password = "airflow",
        database = "mydb"
    )
    
    def write_row_handler(row: tuple):
        mysql.insert_row(row)

    crawler = WeatherCrawler(write_row_handler)
    crawler.start()

    mysql.close()
    
dag = DAG(dag_id="crawl_weather",
          default_args={
              "owner": "Group_6",
              "start_date": datetime(2021, 4, 1, 0, 0, 0)
          },
          schedule_interval=timedelta(hours=3),
          description="Crawl weather data on Korea Meteorological Administration site")

crawl = PythonOperator(task_id="WeatherCrawler",
                       python_callable=crawl,
                       dag=dag)

crawl