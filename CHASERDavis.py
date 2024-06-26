#Create a program to assist students to purchase merchandise
#Jessica Davis CPT-180-A01S

import os, time
merch = {1: 4.99, 2: 3.99, 3: 19.99, 4: 10.95, 5: 5.99, 6: .65, 7: .75}

#Display menu
while True: #outer loop
    print ('\n\n\n\n\n Welcome to the SCC Student Hub \n\n')
    print ('***********   Menu   ***********')
    print ('**** 1. Key tag  ***************')
    print ('**** 2. Magnet   ***************')
    print ('**** 3. Tote bag ***************')
    print ('**** 4. Cup      ***************')
    print ('**** 5. Decal    ***************')
    print ('**** 6. Pencil   ***************')
    print ('**** 7. Coaster  ***************')

#Ask customer for their first name
    print()
    print()
    name = input('Hello! Can I have a name for this order? (Or type "end" to cancel order) ')

    if name == 'end':
           break
    total=0

#Begin tally of items to order
    while True: #inner loop
        print('Please enter a merchandise order: Enter blank to end order')
        new  = input()
        if new == '':
            break
        new=int(new)
        if new in merch:
            print('That item will cost ', format(merch[new],'.2f'))
            total=total + merch[new]

        else:
            print('Im sorry we do not currently carry item ' + str(new))

#Ask if in TRIO program
    trio=input('Are you in the TRIO program? (y or n) ')

    if trio == 'y':
        total = (total*1.4)*1.07

    else:
        total=total*1.07

    print ('Your total cost today is $ ' + str(format(total,'.2f')))

    time.sleep(5)
    os.system('cls')



            
