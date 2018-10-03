#处理日期和时间的标准库,包含date对象和time对象
import datetime
print(datetime.datetime.now())
today = datetime.datetime.now()
print(today.year)
#计算n天后日期
result = today + datetime.timedelta(days= 7)
print(today, result)
#计算时间差
fir = datetime.datetime(2018, 8, 16, 0, 9, 0)
sec = datetime.datetime(2018, 9, 15, 2, 3, 1)
deltime = sec - fir
print(deltime,deltime.total_seconds())