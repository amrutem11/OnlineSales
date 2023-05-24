
import csv
import pandas as panda

#Available worksheet names in the Excel file
sheets = ['Departments', 'Employee', 'Salaries']

# creating empty  DataFrame to store data
all_data = panda.DataFrame()

for sheet_name in sheets:
    
    csv_file = sheet_name + '.csv'
    frame = panda.read_csv(csv_file)
    all_data = all_data.append(frame, ignore_index=True)

# find out average salalry of each department
avg_salary = all_data.groupby('Department')['Salary'].mean()

# Sort the departments by average salary in descending order
sorted_depts = avg_salary.sort_values(ascending=False)

# to obtain  the top 3 departments only applying constarints
departments = sorted_depts.head(3)

# creating the report for top 3 departments according to our needs
report = all_data[all_data['Department'].isin(departments.index)][['Department', 'Salary']]

# Printing the report
print("Top 3 Departments are -> ")
print(report)