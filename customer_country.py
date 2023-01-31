import csv

#Opening and Creating CSV Files
customers = open("customers.csv",'r') 
customer_country = open('customer_country.csv', 'w')

#Reading Through File
csvreader = csv.reader(customers, delimiter=(','))

#Skip Header
next(csvreader)

#Write File
customer_country.write('First Name'+ ' '+ 'Last Name'+' '+ 'Country'+ '\n')
print()
for row in csvreader:
    customer_country.write(row[1]+'  '+ row[2]+ '  '+ row[4] + '\n')


#Close Files
customers.close()
customer_country.close()
