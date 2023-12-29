import datetime as dt

x = dt.datetime.now()
print("Current Date : ", x)
print("Current Year : ", x.year)
print(x.strftime("%A"))

date1 = dt.datetime(2023, 12, 27)
print(date1)
print(date1.strftime("%B"))
