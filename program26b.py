# Program 26B: More Logic Errors

# I want to get the average of these three test scores.
# Calculate the average test score to find out what the output should be
test_score1 = 80.3
test_score2 = 99.2
test_score3 = 77.8

sumOfTestScores = 80.3 + 99.2 + 77.8
average = sumOfTestScores/3
print("Average test score is: ", average)

# I want to add up all the integers from 0 to 9
# Calculate what the output should be
nums = 0
for num in range(0, 10):
    nums += num
print(nums)

# A person is eligible for a discount if they are over 65 or 6 and under
age = 67
if age >= 65:
    print("You are eligible for the seniors discount")
elif age <= 6:
    print("Kids eat free.")

# I want to find all the names that have the letter “y”
name_list = ["Abby", "Ben", "Cory", "Daniel", "Eddy"]
for i in range(len(name_list)):
    if "y" in name_list[i]:
        print(name_list[i])
