CREATE DATABASE IF NOT EXISTS airflow;
CREATE DATABASE IF NOT EXISTS django;
CREATE DATABASE IF NOT EXISTS mydb;
CREATE TABLE IF NOT EXISTS mydb.mw_table( \
    weather_time varchar(20), \
    dist varchar(20), \
    temp_max varchar(20), \
    temp_min varchar(20), \
    weather_sky varchar(20), \
    rnst varchar(20), \
    primary key(weather_time, dist) \
)ENGINE = InnoDB;
CREATE USER 'airflow'@'%' identified with mysql_native_password  by 'airflow';
CREATE USER 'airflow'@'localhost' identified with mysql_native_password  by 'airflow';
GRANT ALL PRIVILEGES ON *.* TO 'airflow'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'airflow'@'localhost' WITH GRANT OPTION;
CREATE USER 'django'@'%' identified with mysql_native_password  by 'django';
CREATE USER 'django'@'localhost' identified with mysql_native_password  by 'django';
GRANT ALL PRIVILEGES ON *.* TO 'django'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'django'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;