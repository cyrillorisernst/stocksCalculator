import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import math

#source of data: https://stooq.com/q/d/?s=uan.us&i=m&d1=20120101&d2=20240402&l=3

howManyYearsBack = 5
fileName = 'uan_us_m.csv'

#open file and store everything but the first row
def getDataFromCSV(fileName):
    with open(fileName, 'r') as file:
        reader = csv.reader(file)


        data=[]

        for i, row in enumerate(reader):
            if i > 0:
                data.append(row)
    return data

def calculateLastYearsHighs(checkHowManyPastYears, data):
    #sort by months of the year
    numberOfMonthsInABusinessYear = 12


    storagePerBussinessmonth = []

    for months in range(numberOfMonthsInABusinessYear):
        storagePerBussinessmonth.append([])

    currentYear = "0000"
    yearCounter = 0
    numberOfYearsTotal = 0

    for i, row in enumerate(data):
        if str(row[0])[:4] != currentYear:
            numberOfYearsTotal+=1
            currentYear = str(row[0])[:4]
            yearCounter = 0
        storagePerBussinessmonth[yearCounter].append(row)
        yearCounter = yearCounter + 1

    print(numberOfYearsTotal)

    monthlyHighestValuesPerYear = []
    for i, month in enumerate(range(numberOfMonthsInABusinessYear)):
        monthlyHighestValuesPerYear.append(0.0)
    print(storagePerBussinessmonth[i][0][0])
    print(monthlyHighestValuesPerYear)

    for i, month in enumerate(reversed(storagePerBussinessmonth)):
        for j in range(checkHowManyPastYears):
            monthlyHighestValuesPerYear[i] = float(monthlyHighestValuesPerYear[i]) + float(month[numberOfYearsTotal-1-j][2])
        monthlyHighestValuesPerYear[i] = float(monthlyHighestValuesPerYear[i]) / checkHowManyPastYears

    monthlyHighestValuesPerYear = monthlyHighestValuesPerYear[::-1]


    print(monthlyHighestValuesPerYear)

    return monthlyHighestValuesPerYear


def showMonthBasedGraph(monthlyHighestValuesPerYear, howManyYearsBack):
    df = pd.DataFrame({
    'x_axis': range(12),
    'y_axis': monthlyHighestValuesPerYear
    })



    # plot
    plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='x')
    plt.title(f"Durchschnitt pro Monat über die letzten {howManyYearsBack} Jahre")
    plt.xlabel("Monat")
    plt.ylabel("Wert in €")
    plt.xticks(np.arange(0, 12, 1))
    plt.yticks(np.arange(0, 200, 10))
    plt.show()

showMonthBasedGraph(calculateLastYearsHighs(howManyYearsBack, getDataFromCSV(fileName)), howManyYearsBack)
