# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 1
total_net = 0

# Add more variables to track other necessary financial data
profit_loss = 0
monthly_changes= []
months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Establish first row of data
    firstRow =  next(reader)
    firstTotal = float(firstRow[1])
    # Establish previous month 

    previousPL = float(firstRow[1])



    # Process each row of data
    for row in reader:
        #total Months
        total_months+=1

             
        # Track the total proft and loss (sum of column 1 for each row)
        total_net += float(row[1])
       
        # Track the net change
        netChange = float(row[1]) - previousPL

        #add on to monthly change
        monthly_changes.append(netChange)

        #add the first month that  change occurred
        months.append(row[0])

        #update previous revenue
        previousPL = float(row[1])

      
       
#Calculate Grand Total
grandTotal = total_net + firstTotal

# # Calculate the average net change across the months
averageChangePerMonth = sum(monthly_changes) / len(monthly_changes)

# # Calculate the greatest increase in profits (month and amount)
greatestIncrease = [months[0],monthly_changes[0]]
greatestDecrease = [months[0],monthly_changes[0]]

#calculate greatest increase and decrease
for m in range(len(monthly_changes)):
  #cacluate the greatest increase and decrease 
    if (monthly_changes[m]> greatestIncrease [1]):
        #if the value is greater than teh greatest increase, that value becomes the new greatest increase
        greatestIncrease[1] = monthly_changes[m]
        # update the month
        greatestIncrease[0] = months[m]

# # Calculate the greatest decrease in losses (month and amount)
    if (monthly_changes[m]< greatestDecrease [1]):
        #if the value is greater than teh greatest increase, that value becomes the new greatest increase
        greatestDecrease[1] = monthly_changes[m]
        # update the month
        greatestDecrease[0] = months[m]



# Generate the output summary
output = (
    f"\nRevenue Data Analysis \n"
    f"---------------------------\n"
    f"\tTotal Months = {total_months}\n"
    f"\tTotal  = {grandTotal:,.2f}\n"
    f"\tAverage Change Per Month = ${averageChangePerMonth:,.2f} \n"
    f"\tGreatest Increase Month = {greatestIncrease[0]} Amount = ${greatestIncrease[1]:,.2f} \n"
    f"\tGreatest Decrease Month = {greatestDecrease[0]} Amount = ${greatestDecrease[1]:,.2f} \n"
    )
    

# Print the output
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

