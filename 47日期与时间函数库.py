# import time
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y%m%d'))

import datetime
# 获取当前时间
print(datetime.datetime.now())

# 获取10分钟后的时间
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

#
one_day = datetime.datetime(2008, 5, 27)
new_date = datetime.timedelta(days=10)
print(one_day + new_date)
