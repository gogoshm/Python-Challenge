#run following python script
#total number of months included in the dataset
#total amount of revanue gained over the entire period
#average change in revenue between months over the entire period
#the greatest increase in revenue (date and amount) over the entire period
#the greatest decrease in revenue (date and amount) over the entire period

import os
import csv

csvpath = os.path.join(".", "budget_data_1.csv")


revenue = []


with open(csvpath, newline="") as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")

#skip header
    next(csvread, None)

    for row in csvread:
        data = [row[0], int(row[1])]
        revenue.append(data)
        
#total month
total_month = len(revenue)

#total revenue
total_revenue = 0
for data in revenue:
    total_revenue += data[1]


#average
average = round(total_revenue/total_month, 2)



print(total_month)
print(total_revenue)
print(average)






















