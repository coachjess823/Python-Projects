#Sums of Digit In String
#Jessica Davis
#Application Development - ITEC 2270

import time

print("\n")
print("This program will allow you to list a string of single digit numbers")
print("and see what the total of the numbers are.\n")

#Ask user to enter single digits
def main():
    numberSeries = input('Enter a series of single-digit numbers with nothing separating them: ')

    #pull in the input and set it up to add
    totalOfDigits = 0
    for i in numberSeries:
        totalOfDigits += int(i)

    #print out the total
    print("The sum of those digits are: ", totalOfDigits)
main()

time.sleep(30)
