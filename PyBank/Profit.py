import csv
import os

# Set up variables to hold financial data
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Open the CSV file
with open("Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Get the month and profit/loss for this row
        month = row[0]
        profit_loss = int(row[1])
        
        # Add to the total number of months
        total_months += 1
        
        # Add to the total profit/loss for this period
        total_profit_loss += profit_loss
        
        # Calculate the change in profit/loss since the previous row
        profit_loss_change = profit_loss - previous_profit_loss
        
        # If this is not the first row, check if the change is the greatest increase or decrease so far
        if total_months != 1:
            if profit_loss_change > greatest_increase["amount"]:
                greatest_increase["date"] = month
                greatest_increase["amount"] = profit_loss_change
            elif profit_loss_change < greatest_decrease["amount"]:
                greatest_decrease["date"] = month
                greatest_decrease["amount"] = profit_loss_change
        
        # Update the previous profit/loss for the next row
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss over the period
average_change = round((total_profit_loss - previous_profit_loss) / (total_months - 1), 2)

# Determine the greatest increase in profits
if int(row[1]) > greatest_increase[1]:
    greatest_increase[0] = row[0]
    greatest_increase[1] = int(row[1])

# Determine the greatest decrease in profits
if int(row[1]) < greatest_decrease[1]:
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = int(row[1])

# Check if the greatest increase list has at least one item
if not greatest_increase[0]:
    greatest_increase[0] = "N/A"
    greatest_increase[1] = 0

# Check if the greatest decrease list has at least one item
if not greatest_decrease[0]:
    greatest_decrease[0] = "N/A"
    greatest_decrease[1] = 0


# Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")



