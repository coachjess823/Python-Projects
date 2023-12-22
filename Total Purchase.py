#Total Purchase#
#Jessica Davis#
#Application Development- ITEC 2270#

import time

#Ask for the price of each of the five items#

print('\n')
print('This program calculates the purchase of 5 sales items.')
print('\n')

salesItem1 = float(input('What is the cost of your first item: $'))
salesItem2 = float(input('What is the cost of your second item: $'))
salesItem3 = float(input('What is the cost of your third item: $'))
salesItem4 = float(input('What is the cost of your fourth item: $'))
salesItem5 = float(input('What is the cost of your fifth item: $'))

#Make some space#
print ('\n')

#Tax Amount#

salesTax = float(0.07)

#Calculation#

subtotal = (salesItem1 + salesItem2 + salesItem3 + salesItem4 + salesItem5)
taxTotal = (subtotal) * (salesTax)
total = (subtotal) + (taxTotal)


#Display the subtotal of the sale, amount of sales tax, and the total#

print ('Your subtotal today is: $', format(subtotal, ',.2f'))
print ('Your tax on this sale is: $', format(taxTotal, ',.2f'))
print ('Which brings your total to: $', format(total, ',.2f'))

print('\n')

#Allow user to see result for 30 seconds#
time.sleep(30)
