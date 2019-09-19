import locale
from dateutil.relativedelta import *
from dateutil.parser import *
from datetime import datetime, date, timedelta

dt_now = datetime.now()
#print(dt_now)
delta = timedelta(days=1)

dtn = dt_now-delta
locale.setlocale(locale.LC_ALL, "russian")
#print(dt_now1.strftime('%A %d %B %Y'))
dtn_es = dtn.strftime('%A %d %B %Y')
print(f'Вчера: {dtn_es}')
dtn_td = datetime.now().strftime('%A %d %B %Y')
print(f'Сегодня: {dtn_td}')
dtn = dt_now+delta
dtn_tm = dtn.strftime('%A %d %B %Y')
print(f'Завтра: {dtn_tm}')

print('--------------------')
date_str = dt_now.strftime('%Y-%m-%d')
datetime_m = datetime.strptime(date_str, '%Y-%m-%d')
print(f'Месяц назад (вариант 1): {datetime_m.replace(month=datetime_m.month-1)}')

now = parse(str(date.today()))
today = now.date()
print("Сегодня:",today)
delta=relativedelta(months=1)
month_ago=today-delta
print("Месяц назад (module):",month_ago)
delta2 = timedelta(days=30)
month_ago2= today-delta2
print("Месяц назад (30 дней):",month_ago2)
print('--------------------')

# Получение даты из строки и вывод на экран
d="01/01/17 12:10:03.234567"
dt = datetime.strptime(d,'%d/%m/%y %H:%M:%S.%f')
print(dt)