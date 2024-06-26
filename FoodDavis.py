#Creat a program for Hendrix Food Truck to tally the total bill for customers
#Jessica Davis CPT-180-A01S Test 1

import time

#Define Food Plate Numbers
combo1= '1'
combo2= '2'
combo3= '3'
combo4= '4'
combo5= '5'

#Loop program
while True:
    

    #Ask customer for first name and the menu item they wish to purchase
    print("To stop program, please enter 'end'.")
    print()
    name=input("Can I have your first name for this order? ")
    print()
    if name == 'end':
          break
    combo=input("Please enter a number 1-5 to select which Food Plate you wish to order: # ")
    if not combo.lower() not in ('1', '2', '3', '4', '5'):
        print()
    else:
        print()
        print('Sorry, that is not a valid choice.  Please enter a number 1-5. ')
        print()
        print()
        continue
    print()


    #Ask customer if they would like to add tip
    tip=input("Would you like to add tip for this order? If so, how much would you like to add: $")
    print()

    #Calculate prices

    if combo == combo1:
        combo1=(15*1.09)+float(tip)
        combo1=format(combo1, '.2f')
        print("Thank you for your order, " + name + ".  Your total bill is $" + str(combo1))
    if combo == combo2:
        combo2=(10*1.09)+float(tip)
        combo2=format(combo2, '.2f')
        print("Thank you for your order, " + name + ".  Your total bill is $" + str(combo2))
    if combo == combo3:
        combo3=(12*1.09)+float(tip)
        combo3=format(combo3, '.2f')
        print("Thank you for your order, " + name + ".  Your total bill is $" + str(combo3))
    if combo == combo4:
        combo4=(10*1.09)+float(tip)
        combo4=format(combo4, '.2f')
        print("Thank you for your order, " + name + ".  Your total bill is $" + str(combo4))
    if combo == combo5:
        combo5=(12*1.09)+float(tip)
        combo5=format(combo5, '.2f')
        print("Thank you for your order, " + name + ".  Your total bill is $" + str(combo5))

    print()
    print()
    
    #Pause for 5 seconds
    time.sleep(5)




  
