# Dependencies.
import os
import csv

# Empty lists for variables
total_months = []
total_profit = []
monthly_pft_chg = []

csvpath = os.path.join('Resources','budget_data.csv')
csvpath

# Open csv file

with open(csvpath, encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    # print(csv_header)
    # Go through rows in stored file contents
    for row in csvreader:
        # Append months and profit to corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        monthly_pft_chg.append(total_profit[i+1]-total_profit[i])

# Obtain max and min of monthly profit change list
max_increase_v = max(monthly_pft_chg)
max_decrease_v = min(monthly_pft_chg)

# Max + min to proper month using month list and index from max + min 
# + 1 at end since month associated with change is +1 month or next month
max_increase_m = monthly_pft_chg.index(max(monthly_pft_chg)) + 1
max_decrease_m = monthly_pft_chg.index(min(monthly_pft_chg)) + 1

# Print
print("Finacial Analysis")
print("--------------------------------------------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_pft_chg)/len(monthly_pft_chg),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_m]} (${str(max_increase_v)})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_m]} (${str(max_decrease_v)})")

# Output file
output_path=os.path.join("analysis", "results.txt")
with open(output_path,'w') as text:
    
    text.write("Finacial Analysis\n")
    text.write("----------------------------------------------------------------\n")
    text.write(f"Total Months: {len(total_months)}\n")
    text.write(f"Total: ${sum(total_profit)}\n")
    text.write(f"Average Change: ${round(sum(monthly_pft_chg)/len(monthly_pft_chg),2)}\n")
    text.write(f"Greatest Increase in Profits: {total_months[max_increase_m]} (${str(max_increase_v)})\n")
    text.write(f"Greatest Decrease in Profits: {total_months[max_decrease_m]} (${str(max_decrease_v)})\n")