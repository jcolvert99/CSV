import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index,column_header)







#-------------------------------
highs = []
dates = []
lows = []

#try, except, else allows us to specify which errors we want to break the code
for record in csv_file:
    try:
        the_date = datetime.strptime(record[2],'%Y-%m-%d')
        high = int(record[4])
        low = int(record[5])
    except ValueError:
        #f string allows us to incorporate variables directly into statements
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(record[4]))
        lows.append(int(record[5]))
        dates.append(the_date)
    

print(highs)
print(dates)

'''
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
'''