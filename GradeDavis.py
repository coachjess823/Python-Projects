#Make a code for Bridgestone College students to receive letter grades.
#CPT-180-A01S Jessica Davis

import time

#Enter students name and numeric grade
print('Please enter your name: ')
name=input()
print()
print('Please enter numeric grade: ')
grade=input()
grade=float(grade)
print()

#Define letter grades
if grade <= 69.5:
    grade = 'F'
elif grade <= 79.5:
    grade = 'C'
elif grade <= 89.5:
    grade = 'B'
else:
    grade = 'A'

#Display back name of student and letter grade
print('Thank you ' + name + ', your letter grade is ' + grade + '!')

time.sleep(5)
