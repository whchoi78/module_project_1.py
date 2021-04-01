from RSS_Crawler import WeatherCrawler
from mysql import MySQLDB
import datetime

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