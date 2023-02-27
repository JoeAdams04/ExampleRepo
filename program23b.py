# Program 23b: Formatting
 
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "Joe", age = 18)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Joe", 18)
#Empty PlaceHolders:
txt3 = "My name is {}, I'm {}".format("Joe", 18)

print(txt1)
print(txt2)
print(txt3)