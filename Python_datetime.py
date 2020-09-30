import datetime


now = datetime.datetime.now()
# print(now)
# print(now.isoformat())
# print(now.strftime('%d_%m_%y-%H_%M_%S_%f'))
#
# today = datetime.date.today()
# print(today)
# print(today.isoformat())
# print(today.strftime('%d_%m_%y'))
#
# print(now)
# d = datetime.timedelta(weeks=1)
# print(now -d)
# d = datetime.timedelta(days=365)
# print(now - d)


import os
import shutil


file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(file_name, now.strftime('%d_%m_%y-%H_%M_%S_%f')))

with open('test.txt', 'w') as f:
    f.write('Hello')
