#Program 27 runtime errors - divide by zero error
a = float(input("Enter a number "))
b = float(input("Enter a number to divide by "))
if b == 0:
    print("You can't divide by 0 silly.")
    b = float(input("Enter another number other than zero: "))

print(f"The answer is {a/b}. ") 