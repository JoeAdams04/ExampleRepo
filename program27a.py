#Program 27 runtime errors - divide by zero error
a = float(input("Enter a number "))
b = float(input("Enter a number to divide by "))

try:
    print(f"The answer is {a/b}.")
except:
    print("This did not work.")
else:
    print("You successfully used the division ")
finally:
    print("Thank you for playing!")