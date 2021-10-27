#Programmer: Callie Walker
#CS151 Programming Assignment 3

#function to calculate quarterback rating
def qb(attempts, completions, passing_yards, touchdown_passes, interceptions):
    rating = 100.0 * (5.0 * (completions / attempts-0.3) + 0.25 * (passing_yards / attempts - 3) + 20.0 * (touchdown_passes / attempts) + 2.375-(25.0 * interceptions / attempts)/ 6.0)
    rating = round(rating,2)
    if (rating >= 158.3):
        print("A Perfect Passer")
    else:
        print("Your rating is ", rating)
    return rating

#function to calculate quidditch team score
def quidditch(goal, snitch):
    goal *= 10
    if (snitch == "yes"):
        goal += 30
    return goal

#function to calculate gymnastics final score
def gymnastics(execute1, execute2, execute3, execute4, execute5, difficulty):
    average = (execute1 + execute2 + execute3 + execute4 + execute5) / 5
    final = average + difficulty
    final = round(final, 2)
    return final


def main():
    choice = input("Which sport would you like to calculate statistics for? ")
    choice = choice.strip().lower()


    if (choice == "football"):
        completions = input("Enter the amount of completions ")
        attempts = input("Enter the amount of attempts ")
        passing_yards = input("Enter the passing yards ")
        touchdown_passes = input("Enter the amount of touchdown passes ")
        interceptions = input("Enter the amount of interceptions ")
        #Checks to make sure the inputs are digits
        if(completions.isdigit() == True and attempts.isdigit() == True and passing_yards.isdigit() == True and touchdown_passes.isdigit() == True and interceptions.isdigit() == True):
            #After checking, the variables are assigned as floats
            completions = float(completions)
            attempts = float(attempts)
            passing_yards = float(passing_yards)
            touchdown_passes = float(touchdown_passes)
            interceptions = float(interceptions)
            #Check to make sure no division by zero
            if(attempts == 0):
                print("cant divide by zero, sorry")
            else:
                print("The Quarterback's rating is ", qb(attempts, completions, passing_yards, touchdown_passes, interceptions))
        else:
            print("Value entered is not a digit")

    elif (choice == "quidditch"):
        goals = input("How many goals were score? ")
        #Checks for digits
        if(goals.isdigit() == True):
            goals = int(goals)
            snitchCaptured = input("Was the snitch caught? ")
            snitchCaptured = snitchCaptured.strip().lower()
            print("Your team's score is ", quidditch(goals, snitchCaptured), "points")
        else:
            print("Value is not a digit")

    elif (choice == "gymnastics"):
        score1 = input("Enter execution 1 score ")
        score2 = input("Enter execution 2 score ")
        score3 = input("Enter execution 3 score ")
        score4 = input("Enter execution 4 score ")
        score5 = input("Enter execution 5 score ")
        difficulty = input("Enter the difficulty ")
        #Checks for digits and assigns the variables as an int
        if(score1.isdigit() == True and score2.isdigit() == True and score3.isdigit() == True and score4.isdigit() == True and score5.isdigit() == True and difficulty.isdigit() == True ):
            score1 = int(score1)
            score2 = int(score2)
            score3 = int(score3)
            score4 = int(score4)
            score5 = int(score5)
            difficulty = int(difficulty)
            if(difficulty == 0):
                print("Cannot divide by zero, sorry")
            else:
                print("Your score is ", gymnastics(score1, score2, score3, score4, score5, difficulty))
        else:
            print("Value entered is not a digit")
    #Sport input was not an option
    else:
        print("Invalid option, sport not available")


main()