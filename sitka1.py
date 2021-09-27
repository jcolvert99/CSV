import csv

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row))

#enumerate gives you the index location and the object itself at that location
#helps you know where each item is located
for index, column_header in enumerate(header_row):
    print(index,column_header)


highs = []

for record in csv_file:
    highs.append(int(record[5]))
    
#print(highs)


import matplotlib.pyplot as plt

plt.title("Daily high temperature, July 2018",fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)
#this is where the configuration stops, add data below
plt.plot(highs,c="red")
plt.show()