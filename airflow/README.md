1. docker-compose up --build

2. localhost:8080에 접속
(id, ps : airflow)

3. crawl_weather 왼쪽의 버튼 클릭

******
MySQL 정보
Version : 8.0.23
Container Name : airflow_mysql_1
Port : 3306

Use Database : mydb
Use Table : mw_table
Use User : airflow
Use Password : airflow
Use Root Password : passw0rd


******
File Information(Directory)

crawl.py(.)
 - DAG File.
 - Schedule 시작일("start_date": datetime(2021, 4, 1, 0, 0, 0)), 간격(schedule_interval=timedelta(hours=3)) 설정
 - DB 접속 설정(Host, Database, User, Password)

Dockerfile(.)
 - Docker compose시 필요한 명령어 정리
 - requierments.txt 설치

init.sql(./init)
 - Compose up 시에 MySQL에 DB, TABLE, User Create
 - 해당 정보는 상단의 MySQL 정보 참고

dist_num_crawling.py(./weather_crawler)
 - 기상청의 위치에 따른 지역 코드를 가져오기 위해 작성한 임시 파이썬 파일

exceptions.py(./weather_crawler)
 - 각종 오류 발생 시 Raise

mysql.py(./weather_crawler)
 - MySQL 명령어 삽입
 - 희원씨가 작성한 MySQL 명령어를 더 쉽게 사용하기 위해 정리하여 작성

RSS_Crawler.py(./weather_crawler)
 - 실제 크롤링이 이뤄지는 파이썬 파일
 - URL, Crawling Data 정보 설정
 
RSS_Crawler(temp).py(./weather_crawler)
 - 프로젝트 초기에 지역 코드를 이용한 크롤링시 사용했던 파이썬 파일
 - 현재 사용하지 않음

(logs)
 - Airflow 작업으로 인한 로그 기록

(plugins)
 - 미사용

(__pycache__)
 - 미사용