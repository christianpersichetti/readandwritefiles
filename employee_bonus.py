import csv

employee_bonus = open('EmployeePay.csv','r')

csvreader = csv.reader(employee_bonus, delimiter=(','))

print('ID '+ 'First Name '+ 'Last Name '+ 'Salary '+ 'Bonus')    
next(csvreader)

for row in csvreader:
    print(row[0],' ', row[1], ' ', row[2], ' ', row[3], ' ', row[4])



employee_bonus.close()