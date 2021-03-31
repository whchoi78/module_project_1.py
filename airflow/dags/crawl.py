import os
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from weather_crawler.mysql import MySQLDB
from weather_crawler.RSS_Crawler import WeatherCrawler


def crawl():
    mysql = MySQLDB(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "p@ssw0rd",
        database = "mydb"
    )
    
    def write_row_handler(row: tuple[datetime, str, str, str, str, str]):
        mysql.insert_row(row)

    crawler = WeatherCrawler(write_row_handler)
    crawler.start()

    mysql.close()
    
dag = DAG(dag_id="crawl_weather",
          default_args={
              "owner": "Group_6",
              "start_date": datetime.today()
          },
          schedule_interval="3 * * * *",
          description="Crawl weather data on Korea Meteorological Administration site")

crawl = PythonOperator(task_id="WeatherCrawler",
                       python_callable=crawl,
                       dag=dag)

crawl