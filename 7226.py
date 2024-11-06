 
from datetime import datetime, timedelta

day = int(input())
start_date = datetime(2014, 1, 1)
target_date = start_date + timedelta(days=day - 1)
print(target_date.day, target_date.month)