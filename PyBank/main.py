import os 
import csv 

budget_csv = os.path.join('Resources', 'PyBank_Resources_budget_data.csv')

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read after the header row
    header = next(csvreader)
       
    # Set the base values for the parameters 
    month_count = 0
    total = 0
    max_month = ""
    min_month = ""
    
    # Read rows 
    for row in csvreader:
        # Set values for parameters
        month_count += 1
        total += int(row[1])
        date = []
        changes = []
       
    # Print Label
    print("Financial Analysis")
    print("-------------------------")

    # Print out the total months
    print(f"Total Months: {str(month_count)}")
    
    # Print out the total profits/loss
    print(f"Total: ${str(total)}")

    profit_loss = row[1]

    # Loop through the rows to find the following info
    for i in range(1, profit_loss):
        changes = profit_loss[i+1] - profit_loss[i]
        ave_change = sum(changes)/month_count
        max_inc = max(changes)
        max_inc_date = str(date[changes.index(max(changes))])
        max_dec = min(changes)
        max_inc_date = str(date[changes.index(min(changes))])

    # Print out the average change
    print(f"Average Change: ${str(ave_change)}")
    
    # # Print out the greatest increase in profits month-year and $value
    # print(f"Greatest Increase in Profits: {str(max_inc)}")
    
    # # Print out the greatest decrease in profits month-year and $value
    # print(f"Greatest Decrease in Profits: {str(max_dec)}")