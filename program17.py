# Program 17: Nested For Loops
initialSalesGoal = 200000
multiplier = 100
offMonth = True # If you change it to false you just wont have an Off Month.

for monthlyGoal in range(1, 13):
    if monthlyGoal == 6 and offMonth:
        print("There is no goal for month 6 ")
        continue
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
    print("Your sales goal for the month " + str(monthlyGoal) + " is $" + str(monthlySalesGoal))
    for weeklyGoal in range(1, 5):
        print("Your sales goal for the week " + str(weeklyGoal) + " is $" + str(monthlySalesGoal/4))
print("Good luck with your goals!")