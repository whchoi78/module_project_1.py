
import os
import pymysql

class MySQLDB(object):
    def __init__(self, host, port, user, password, database):
        self.buffer = list()
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password, 
            charset="utf8",
            database=database,
        )

    def query(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def insert_row(self, row: tuple[datetime, str, str, str, str, str]):
        self.buffer.append(row)
        if len(self.buffer) > 50:
            self.do_flush()

    def do_flush(self):
        if not self.buffer:
            return
        query_text = "INSERT INTO mw_table(weather_time, dist, temp_max, temp_min, weather_sky, rnst) VALUES "
        query_text += ", ".join(map(lambda x: f"('{x[0]}', '{x[1]}', '{x[2]}', '{x[3]}', '{x[4]}', '{x[5]}')", self.buffer))
        self.buffer.clear()
        try:
            self.query(query_text)
        except Exception:
            pass

    def close(self):
        self.conn.close()