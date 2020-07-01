import datetime
print(datetime.datetime.now())

print(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))



import time
today_timestamp = time.time()
print(today_timestamp)
today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print(today_date)
tomorrow_timestamp = today_timestamp + 86400
print(tomorrow_timestamp)
tomorrow_date = time.strftime('%Y-%m-%d',time.localtime(tomorrow_timestamp))
print(tomorrow_date)


fetureDate = time.strftime('%Y-%m-%d',time.localtime(time.time()+86400*365*10))
print(fetureDate)

