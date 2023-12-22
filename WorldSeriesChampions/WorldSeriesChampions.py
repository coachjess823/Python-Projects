#World Series Championship
#Jessica Davis
#Application Development - ITEC 2270

import time

print("\n")
print("This program will allow you to look up teams and see how many times")
print("and what years a team has won the World Series.\n")

def main():

    #Pull data from text file
    
    fileName = open("WorldSeriesWinners.txt", 'r')
    winnersTxt = fileName.readlines()

    #Search the list for time the chosen team won
    
    for file in range(len(winnersTxt)):
        winnersTxt[file] = winnersTxt[file].rstrip('\n')
    search = input("Please enter the name of a team and see how many World Series they have won.\n")
    count = 0
    
    #Set up the years the teams played and take out the years not played
    
    noWorldSeries = 2010
    startOfList = []
    for file in range(len(winnersTxt)):
        noWorldSeries -= 1
        if winnersTxt[file] == search:
            count += 1
            if noWorldSeries == 1904 or noWorldSeries == 1994:
                  break
            startOfList.append(noWorldSeries)

    #Print the number of time the team has won and what years
            
    print("\nThe", search, "have won the World Series championship ", count, " times")
    print("The years they won are: ", startOfList)
    
main()

time.sleep(30)
