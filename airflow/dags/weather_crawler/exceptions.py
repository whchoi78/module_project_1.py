import os

# 지역 번호가 잘못되었을 경우
class InvalidCodenumber(Exception):
    def __init__(self, args):
        self.message = f'Number {args} is Invalid'

    def __str__(self):
        return self.message

# 실행시간이 너무 길어서 데이터를 얻을 수 없을 때
class ResponseTimeout(Exception):
    def __init__(self):
        self.message = "Couldn't get the data"

    def __str__(self):
        return self.message

# DB가 열리지 않은 상태일 경우  
class DBisnotopened(Exception):
    def __init__(self):
        self.message ="DB is not opened"
        
    def __str__(self):
        return self.message
