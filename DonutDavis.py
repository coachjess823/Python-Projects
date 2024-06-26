#Design a program for SCC Student Hub to use at their kiosk
#for customers to purchase breakfast items
#Jessica Davis CPT-180-A01S

import time

#Dictionary
item = {'Specialty donut':1.50,'Bagel':3.15,'Croissant':2.98,'English muffin':1.75,'Coffee':2.99,'Juice':1.99}
breakfast = ['Specialty donut','Bagel','Croissant','English muffin','Coffee','Juice']

basket=[]
total=[]

#Prompt user to enter name
while True:
    print('Enter a name for the order: (blank to quit) ')
    name = input()
    if name =='':
        break
    print()

#Start loop and add items
    while True:
        print('Please enter which item you would like to order: ')
        menu = input()
        if menu =='':
            break
        
        for k,v in item.items():
            print('Item: ' + k + ' Price: ' + v + '\n\n')
        
        if menu in item:
            print=('The amount for ' + k + ' is ' + v)
        else:
            print ('Sorry we do not currently carry that item ' + menu)
            print ('Please type in one of the current options: \n\n' + str(breakfast))
        print()


        
                
            

#Ending message and show total
    print ('Thank you, your order cost is: ' + total)
    
time.sleep(5)
