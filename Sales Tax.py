#Sales Tax#
#Jessica Davis#
#Application Development- ITEC 2270#

import time

#Ask user to enter purchase amount#

print ('\n')
print ('This program will calculate Sales Tax of a purchase.')
print ('\n')

purchase = float(input('Please enter the amount of your purchase: $'))

#Tax Amounts#

perStateSalesTax = 0.05
perCountySalesTax = 0.025

#Compute state and county sales tax#

stateSalesTax = purchase * perStateSalesTax
countySalesTax = purchase * perCountySalesTax

#Compute Total Sales tax and Total Sales Amount#

salesTaxTotal = stateSalesTax + countySalesTax
totalPurchase = purchase + salesTaxTotal

#Display totals#

print ('\n')
print ('The amount you entered for your purchase is: $', format(purchase, ',.2f') )
print ('Which brings the total state sales tax owed to: $', format(stateSalesTax, ',.2f'))
print ('Which brings the total county sales tax owed to: $', format(countySalesTax, ',.2f'))
print ('Which brings your total taxes to: $', format(salesTaxTotal, ',.2f'))
print ('And your total purchase to: $', format(totalPurchase, ',.2f'))
print ('\n')

#Allow user to see result for 30 seconds#
time.sleep(30)

