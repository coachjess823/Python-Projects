#Employee and ProductionWorker Classes
#Jessica Davis
#Application Development - ITEC 2270

import time

print("\n")
print("This program allows the user to enter in the employee's name, employee's number, ")
print("which shift the employee works, and how much the employee's hourly rate is and displays it.")
print("\n")

#Write an Employee class
class Employee:

    def __init__(self, name, employeeNumber):

        self.name = name
        self.employeeNumber = employeeNumber

    def get_name(self):

        return self.name

    def get_employeeNumber(self):

        return self.employeeNumber

#Write a ProductionWorker class
class ProductionWorker(Employee):

    def __init__(self, name, employeeNumber, shiftNumber, hourlyPay):

        super().__init__(name, employeeNumber)
        self.shiftNumber = shiftNumber
        self.hourlyPay = hourlyPay

    def get_shiftNumber(self):

        return self.shiftNumber

    def get_hourlyPay(self):

        return self.hourlyPay


# Create an object of the ProductionWorker class
name = input("Please enter employee name: ")
employeeNumber = input("Please enter employee number: ")
shiftNumber = int(input("Please enter employee shift number (1 for day shift, 2 for swing shift, or 3 for night shift): "))
hourlyPay = float(input("Please enter hourly pay rate: $"))

if shiftNumber == 1:
    shiftNumber = "(1)Day Shift"
if shiftNumber == 2:
    shiftNumber = "(2)Swing Shift"
if shiftNumber == 3:
    shiftNumber = "(3)Night Shift"
    
#Tie in all the data of productionWorker
productionWorker = ProductionWorker(name, employeeNumber, shiftNumber, hourlyPay)

# Display the data using accessor methods
print("\nEmployee Name:", productionWorker.get_name())
print("Employee Number:", productionWorker.get_employeeNumber())
print("Shift Number:", productionWorker.get_shiftNumber())
print("Hourly Pay Rate: $", format(productionWorker.get_hourlyPay(), ',.2f'))

time.sleep(30)
