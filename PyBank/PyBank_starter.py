# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "/Users/erikfraas/Rutgers/Rutgers Homework/Python_challenge/PyBank/Resources/budget_data.csv"
file_to_output = "/Users/erikfraas/Rutgers/Rutgers Homework/Python_challenge/PyBank/analysis/budget_analysis.txt"

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []  # List to store changes in "Profit/Losses" between months
month_of_change = []  # List to track month-over-month changes
greatest_increase = ["", 0]  # Store month and value of greatest profit increase
greatest_decrease = ["", float('inf')]  # Store month and value of greatest loss decrease

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list  
    first_row = next(reader)     

    # Track the total and net change
    total_months += 1 
    total_net += int(first_row[1])  # Add the first month profit/loss
    previous_net = int(first_row[1])  # Store the first month's profit and loss for comparison 

    # Process each row of data
    for row in reader: 
        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_net  # Calculate month-over-month change
        previous_net = int(row[1])  # Update previous month's profit/loss for next iteration
        net_change_list.append(net_change)  # Add this month's change to the list
        month_of_change.append(row[0])  # Add the month to the change list 

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the average net change across the months
if len(net_change_list) > 0:
    avg_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)