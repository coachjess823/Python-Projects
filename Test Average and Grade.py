#Test Average and Grade#
#Jessica Davis#
#Application Development - ITEC 2270#

import time

print ("\n")
print ("This program will ask a user for five test scores and display the average score and letter grade.")
print ("\n")

#Ask user for scores#
def get_score():
    score = float(input("Please enter a score: "))
    while score < 0 or score > 100:
        print ("You have entered an Invalid score.  All Scores must be between 0 and 100.")
        score = float(input("Please enter your score: "))
    return score

#Set up letter grades#
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
#Get 5 scores from user#
def main():
    scores = []
    for i in range(5):
        scores.append(get_score())

    #Average of score calculation#
    average_score = sum(scores) / len(scores)

    #Print out results#
    print()
    print("{:<10}{:<10}{:<10}".format("Score","Numeric","Letter"))
    for i in range(5):
        letter_grade = get_letter_grade(scores[i])
        print ("{:<10}{:<10}{:<10}".format("score " + str(i+1) + ":", scores[i], letter_grade))
        
    #Average and Letter grade#
    print("\n")
    print("Average score:", average_score, get_letter_grade(average_score))
    print("\n")

#Repeat#
main()

#Set 30 second timer#
time.sleep(30)
