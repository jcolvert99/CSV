import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)


#-------------------------------
highs = []
dates = []
lows = []

for record in csv_file:
    highs.append(int(record[5]))
    the_date = datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(the_date)
    lows.append(int(record[6]))

print(dates)

#--------------------------------
   
    


import matplotlib.pyplot as plt
fig = plt.figure()
plt.title("Daily high temperature, July 2018",fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

#this is where the configuration stops, add data below
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)

#fill the space between the lines with a very light color (low alpha)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

fig.autofmt_xdate()

plt.show()


#subplot lets us use multiple plots on the same figure
#has three arguments- row, column, index / (2,1,1) creates to graphs on top of each other / index starts at 1
plt.subplot(2,1,1)
plt.plot(dates,highs,c='red')
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c='blue')
plt.title("Lows")

#super title is the title of the whole output
plt.suptitle("Highs and Lows of Sitka, Alaska")
plt.show()