#Population#
#Jessica Davis#
#Application Development - ITEC 2270#

import time

#Ask for the starting amount of organisms, average daily percentage increase,#
#and the number of days for the organisms to multiply#

print('\n')
print('This program predicts the approximate size of a population based off of percentage increased and days to multiply.')
print('\n')

startingOrganisms = int(input('Please enter the starting number of organisms: '))
dailyPercentage = int(input('Please enter the number of average percentage of daily increase: '))
daysMultiplied = int(input('Please enter the number of days you wish the organisms to multiply: '))

#Make some space#

print('\n')

#Print out the header of the table#

print('Days Approximate \t\tPopulation')

#Set the if statement for the calculations of organisms#

for x in range(1, daysMultiplied +1):
    if x > 1:
        increase = startingOrganisms * dailyPercentage / 100
        startingOrganisms += increase

#Print results#

    print(x, '\t\t\t\t',format(startingOrganisms, '.3f'))


#Allow user to see result for 30 second#

print('\n')
print('Thank you!')

time.sleep(30)
