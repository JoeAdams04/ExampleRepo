# Program 15 For Loops
initialSalesGoal = 20000
multiplier = 100

for monthlyGoal in range (1, 13):
    if monthlyGoal == 6:
            print("There is no goal for month 6")
            continue
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
    print("Your sales goal for the month " + str(monthlyGoal) + " is " + str(monthlySalesGoal))

print("Good luck with your goals!")