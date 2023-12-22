#Shipping Charges#
#Jessica Davis#
#Application Development - ITEC 2270#

import time

#Ask for the weight of the package and set variables#

print('\n')
print('This program calculates the shipping cost of packages based on their weight.')
print('\n')

packageWeight = float(input("Please enter weight of package in pounds: "))
shipRate = 0.0

#Make some space#

print('\n')

#Set the ship rate amount for each weight class#

if packageWeight <= 2:
    shipRate = 1.50
elif packageWeight > 2 and packageWeight <= 6:
    shipRate = 3.00
elif packageWeight > 6 and packageWeight <= 10:
    shipRate = 4.00
elif packageWeight > 10:
    shipRate= 4.75


#Calculations#

shippingCharge = packageWeight * shipRate

#Display the amount of the shipment#

print('The total amount to ship your package is: $', format(shippingCharge, ',.2f'))

print ('\n')
print ('Thank you!')

#Allow user to see result for 30 seconds#

time.sleep(30)
