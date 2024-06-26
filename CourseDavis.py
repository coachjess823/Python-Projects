#This program will assist a student at SCC in selecting an appropriate
#humanity or social science course as part of their AAS degree
#Jessica Davis CPT-180-A01S

import time

#Set up list
socialscience=['ECO 210', 'GEO 101', 'SOC 101', 'PSY 201', 'HIS 101', 'PSC 201']
humanities=['ART 101', 'ENG 101', 'MUS 105', 'PHI 101', 'REG 101']

#Set up loop function
while True:
    #Allow the student to choose social science
    print ()
    print ("To stop program, please enter 'end'.")
    print ()
    print ("Please enter the course in Social Science that you would like to take: ")
    print()
    course=input()
    print()
    if course == 'end':
        break

    #Allow the student to add more social science classes
    if course not in socialscience:
        print ('That course is not an acceptable course.')
        print ('Please choose an acceptable course from the list below.')
        print ()
        print(socialscience)
        print ()
        answer = input ('Would you like to add another Social Science to the list? (y or n): ')
        if answer == 'y':
            socialscience.append(course)
        print ()

    #Allow the student to choose humanity
    print("Please enter the course in Humanities that you would like to take: ")
    print ()
    course=input()
    print()

    #Allow the student to add more humanity classes
    if course not in humanities:
        print ('That course is not an acceptable course.')
        print ('Please choose an acceptable course from the list below.')
        print ()
        print(humanities)
        print ()
        answer = input ('Would you like to add another Humanities to the list? (y or n): ')
        if answer == 'y':
            humanities.append(course)
        print ()

    print("Thank you!")
    print ()
    
    time.sleep(5)

