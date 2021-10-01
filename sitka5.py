import csv
from datetime import datetime
import matplotlib.pyplot as plt

#--------------open csv files-------------------------
open_file = open("sitka_weather_2018_simple.csv","r")
csv_file1 = csv.reader(open_file,delimiter=",")

open_file = open("death_valley_2018_simple.csv","r")
csv_file2 = csv.reader(open_file,delimiter=",")

header_row1 = next(csv_file1)
header_row2 = next(csv_file2)


#-------------determine indexes--------------------
for index, column_header in enumerate(header_row1):
    if column_header == 'TMIN':
        TMIN_index1 = index
    if column_header == 'TMAX':
        TMAX_index1 = index
    if column_header == 'DATE':
        DATE_index1 = index

for index, column_header in enumerate(header_row2):
    if column_header == 'TMIN':
        TMIN_index2 = index
    if column_header == 'TMAX':
        TMAX_index2 = index
    if column_header == 'DATE':
        DATE_index2 = index



#--------------------------get the data---------------------
highs1 = []
lows1 = []
dates1 = []
graph1_title = ''

for record in csv_file1:
    try:
        the_date = datetime.strptime(record[DATE_index1],'%Y-%m-%d')
        high = int(record[TMAX_index1])
        low = int(record[TMIN_index1])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(the_date)
    if graph1_title == '':
        graph1_title = record[1]


highs2 = []
lows2 = []
dates2 = []
graph2_title = ''

for record in csv_file2:
    try:
        the_date = datetime.strptime(record[DATE_index2],'%Y-%m-%d')
        high = int(record[TMAX_index2])
        low = int(record[TMIN_index2])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(the_date)
    if graph2_title == '':
        graph2_title = record[1]


#------------------build the graphs---------------------
fig = plt.figure()
plt.subplot(2,1,1)
plt.plot(dates1,highs1,c='red',alpha=0.5)
plt.plot(dates1,lows1,c='blue',alpha=0.5)
plt.fill_between(dates1,highs1,lows1,facecolor='blue',alpha=0.1)
plt.title(graph1_title)

plt.subplot(2,1,2)
plt.plot(dates2,highs2,c='red',alpha=0.5)
plt.plot(dates2,lows2,c='blue',alpha=0.5)
plt.fill_between(dates2,highs2,lows2,facecolor='blue',alpha=0.1)
plt.title(graph2_title)
fig.autofmt_xdate()

plt.suptitle(f"Temperature comparison between {graph1_title} and {graph2_title}")
plt.show()




