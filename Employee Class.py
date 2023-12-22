#Employee Class
#Jessica Davis
#Application Development - ITEC 2270

import time

print("\n")
print("This program will allow the user to see the stored information ")
print("of employees name, id number, department, and job title.\n")


class Employee:

#Class for employee.

    def __init__(self, name, idNumber, department, jobTitle):

        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle

    

# Create three Employee objects
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Display the data for each employee
print("Employee 1:")
print("Name:", employee1.name)
print("ID Number:", employee1.idNumber)
print("Department:", employee1.department)
print("Job Title:", employee1.jobTitle)

print("\nEmployee 2:")
print("Name:", employee2.name)
print("ID Number:", employee2.idNumber)
print("Department:", employee2.department)
print("Job Title:", employee2.jobTitle)

print("\nEmployee 3:")
print("Name:", employee3.name)
print("ID Number:", employee3.idNumber)
print("Department:", employee3.department)
print("Job Title:", employee3.jobTitle)

time.sleep(30)
