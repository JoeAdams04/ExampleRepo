# Program 9: Using the Identity Operator
a = 3
b = a
northItems = ["Rain gear", "Snow shoes"]
eastItems = ["Rain gear", "Snow shoes"]

print (northItems == eastItems)
print (northItems is eastItems)
print (northItems is not eastItems)

print (a==b)
print (a is b)