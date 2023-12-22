#Course Information
#Jessica Davis
#Application Development - ITEC 2270

import time

print("\n")
print("This program will allow the user to look up their course and see ")
print("what room they are in, who their teacher is, and what time the class starts.\n")

# Dictionary containing course numbers and room numbers

courseRoom = {
    "CS101": "Room 3004",
    "CS102": "Room 4501",
    "CS103": "Room 6755",
    "NT110": "Room 1244",
    "CM241": "Room 1411"
}

# Dictionary containing course numbers and instructor names

courseInstructor = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

# Dictionary containing course numbers and meeting times

courseTimes = {
    "CS101": "8:00 AM",
    "CS102": "9:00 AM",
    "CS103": "10:00 AM",
    "NT110": "11:00 AM",
    "CM241": "1:00 PM"
}

# Prompt the user to enter a course number

courseNumber = input("Please enter the course number to see room number, instructor, and time: \n")

# Display the course's room number, instructor, and meeting time

if courseNumber in courseRoom:
    print(f"\nRoom Number: {courseRoom[courseNumber]}")
    print(f"Instructor: {courseInstructor[courseNumber]}")
    print(f"Meeting Time: {courseTimes[courseNumber]}")
    
else:
    print("Invalid course number.")

time.sleep(30)
