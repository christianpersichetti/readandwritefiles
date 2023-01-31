import csv
#Open File
employee_bonus = open('EmployeePay.csv','r')

#Read Through File
csvreader = csv.reader(employee_bonus, delimiter=(','))

#Header
print('ID '+ 'First Name '+ 'Last Name '+ 'Salary '+ 'Bonus')    
next(csvreader)

#Printing File
for row in csvreader:
    print(row[0],' ', row[1], ' ', row[2], ' ', row[3], ' ', row[4])

#Close File
employee_bonus.close()