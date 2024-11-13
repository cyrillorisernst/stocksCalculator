import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import math

#open file and store everything but the first row
with open('uan_us_m.csv', 'r') as file:
    reader = csv.reader(file)


    data=[]

    for i, row in enumerate(reader):
        if i > 0:
            data.append(row)


#sort by months of the year
numberOfMonthsInABusinessYear = 12
storagePerBussinessmonth = []

for months in range(numberOfMonthsInABusinessYear):
    storagePerBussinessmonth.append([])

currentYear = "0000"
yearCounter = 0
for i, row in enumerate(data):
    if str(row[0])[:4] != currentYear:
        currentYear = str(row[0])[:4]
        yearCounter = 0
    storagePerBussinessmonth[yearCounter].append(row)
    yearCounter = yearCounter + 1



checkHowManyPastYears = 3

highestValueInShare = 0.0

# for month in storagePerBussinessmonth:
#     print(month)

for i, month in enumerate(storagePerBussinessmonth):
    for j in reversed(range(checkHowManyPastYears)):
        if float(month[i][3]) > float(highestValueInShare):
            highestValueInShare = month[j][3]

print(highestValueInShare)









df = pd.DataFrame({
   'x_axis': range(1, 12),
#    'y_axis': range(1, math.ceil(float(highestValueInShare)))
})

# plot
plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o')
plt.show()