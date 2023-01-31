import csv

#Opening and Creating CSV Files
sales = open('sales.csv','r') 
sales_report = open('salesreport.csv', 'w')

#Reading file
csvreader = csv.reader(sales, delimiter=(','))

#Skip Header 
next(csvreader)

#New Header
sales_report.write('CustomerID'+ ' '+ 'Total' + '\n')

#Consolidating Customer ID and Adding Total 
customer_id = 250
total_value = 0
for row in csvreader:
    if int(row[0]) == customer_id:
        total_value = (total_value + float(row[3]) + float(row[4]) + float(row[5]))
    elif int(row[0]) != customer_id:
        decimals = format(total_value,'.2f')
        sales_report.write(' ' +str(customer_id) + ' ' + str(decimals) + '\n')
        customer_id += 1 
        total_value = 0
        total_value += float(row[3]) + float(row[4]) + float(row[5])
    else:
        StopIteration

#Close Files      
sales.close()
sales_report.close()



