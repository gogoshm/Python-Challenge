#run following python script
#total number of months included in the dataset
#total amount of revanue gained over the entire period
#average change in revenue between months over the entire period
#the greatest increase in revenue (date and amount) over the entire period
#the greatest decrease in revenue (date and amount) over the entire period

import os
import csv

budget_1_csv = os.path.join("...", "Pybank", "budget_data_1.csv")

month = []
revenue = []

with open(budget_1_csv, newline="") as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")
    for row in csvread:
        month.append(row[0])
        revenue.append(row[1])

total_month = len(month)
total_revenue = 0






print(total_month)










