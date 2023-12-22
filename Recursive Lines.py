#Recursive Lines
#Jessica Davis
#Application Development - ITEC 2270

import time

print("\n")
print("This program will allow you the user to type in a positive integer")
print("and see the number lines of asterisks.\n")

def recursiveAsterisks(n):

    # Call in item n and start recursive loop without starting at 0
    if n > 0:
        recursiveAsterisks(n - 1)  
        print('*' * n)  


# Call in the input and display to make lines of asterisks
n = int(input('Please enter a positive number: '))
print("\n")

recursiveAsterisks(n)

time.sleep(30)
