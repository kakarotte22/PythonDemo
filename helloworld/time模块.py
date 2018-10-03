import time
#获取时间戳   时间戳为当前时间到1970年1月1日0时0分0秒的秒数差，浮点型
result = time.time()
year = result/(24 * 60 * 60 * 365) + 1970
print(year)
#year大致等于当前年份
print(result)
#获取时间元组 ：0~9 ：time.localtime([seconds = 当前时间戳])
print(time.localtime())
#time.struct_time(tm_year=2018, tm_mon=8, tm_mday=15, tm_hour=23, tm_min=12, tm_sec=47, tm_wday=2（0~6,0：周日）, tm_yday=227, tm_isdst=0(夏令时标记))
#获取格式化的时间
#秒—>可读时间：import time       time.ctime（[seconds=localtime]）
result = time.ctime()
print(result)
#时间元组—>可读时间:import time       time.asctime（[tuple=local-tuple]）
result = time.asctime()
print(result)
#--------------------格式化时间日期---------------------------------------------------
#时间元组—>格式化时间日期：time.strftime(格式字符串，时间元组)
result = time.strftime('%Y-%m-%d  %A  %H:%M:%S',time.localtime())
print(result)
#格式化时间日期—>时间元组：time.strptime(时间元组，格式字符串)
#time.mktime(时间元组)  返回时间戳
#time.clock() 获取当前cpu时间，浮点数秒数，通常用于计算代码耗时
#time.sleep(sec)  休眠sec秒




#python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
