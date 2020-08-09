#import
import os
import csv

#variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0 
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#path for file
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#open and read CSV
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #read header
    csv_header = next(csvreader)
    row = next(csvreader)

    #calc total number of mnths, net amount profit/loss, set variable for rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #read each row of data after header
    for row in csvreader:

        #calc total num of mnths included in data
        total_months += 1
        #calc net amount of profit/loss over the period
        net_amount += int(row[1])

        #calc change from current mnth to previous mnth
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        #calc greatest inc
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #calc greatest dec
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    #calc average and date
    average_change = sum(monthly_change)/ len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#print analysis
print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: {average_change:.2f}")
print(f"Greatest Inc in Profits:, {greatest_increase_month}, ( ${highest})")
print(f"Greatest Dec in Profits:, {greatest_decrease_month}, (${lowest})")
