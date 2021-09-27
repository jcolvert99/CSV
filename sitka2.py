import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row))


#testing to convert date from string
mydate = datetime.strptime('2018-07-01','%Y-%m-%d')
print(mydate)

#-------------------------------
highs = []
dates = []

for record in csv_file:
    highs.append(int(record[5]))
    the_date = datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(the_date)

print(dates)

#--------------------------------


   
    


import matplotlib.pyplot as plt
fig = plt.figure()
plt.title("Daily high temperature, July 2018",fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)
#this is where the configuration stops, add data below
plt.plot(dates,highs,c="red")


fig.autofmt_xdate()

plt.show()
