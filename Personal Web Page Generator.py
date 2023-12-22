#Personal Web Page Generator#
#Jessica Davis#
#Application Development - ITEC 2270#

import time

print("\n")
print("This program will allow you to generate a personal web page.")
print("\n")

#Get name from user#
userName = input("Please enter your name:")

#Get description from user#
userDescription = input("Please described a little about yourself:")

#Set up file for html content#
f=open('aboutme.html','w')

#HTML#
html="<html>\n" + \
"<head>\n" + \
"</head>\n" + \
"<body>\n" +\
"<center>\n" +\
"<h1>" + userName + "</h1>\n" + \
"</center>\n" +\
"<hr/>\n" + \
userDescription + "\n" \
"<hr/>\n" + \
"</body>\n" +\
"</html>\n"

#Writing the file
f.write(html)

#Closing the file
f.close()

time.sleep(30)