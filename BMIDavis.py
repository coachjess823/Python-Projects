#BMI Calculator
#Jessica Davis\CPT-180-A01S

import time


#Loop program:
while True:
    
    #Defining terms and asking for input
    print("To stop program, enter 'end'. ")
    height = input("Please, enter your height in inches: ")
    if height == 'end':
        break
    weight = input("Please, enter your weight in lbs: ")
    print()


    #Calculate BMI
    bmi = (float(weight) / float(height) ** 2) * 703

    #Print Results
    print("Your BMI is " + str(bmi) + ".")


    #Define levels of BMI
    if bmi <= 18.5:
        print("Based on your BMI you are considered underweight.")
        print()
    elif bmi <= 24.9:
        print ("Based on your BMI you are considered Normal weight.")
        print()
    elif bmi <= 29.9:
        print ("Based on your BMI you are considered Overweight.")
        print()
    else:
        print ("Based on your BMI you are considered Obese.")
        print()

    time.sleep(5)           
