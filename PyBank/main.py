import os
import csv

pybank = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "budget_data.txt")

total_months = 0
months_changed =[]
total = 0
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    first_row = next(csvreader)
    total_months = total_months + 1
    total = total + int(first_row[1])
    previous_total = int(first_row[1])
    for row in csvreader:

        #total and net change
        total_months = total_months + 1
        total = total + int(row[1])
        net_change = int(row[1]) - previous_total
        previous_total = int(row[1])
        net_change_list = net_change_list + [net_change]
        months_changed = months_changed + [row[0]]

        #calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #calculate greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#calculate average net change
net_monthly_average = sum(net_change_list) / len(net_change_list)

#output summary
output = (
    f"Financial Analysis\n "
    f"------------------------------------- \n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${net_monthly_average}\n"
    f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )
#print output
print(output)

#print results to text file
with open(output_file, "w") as textfile:
    textfile.write(output)
