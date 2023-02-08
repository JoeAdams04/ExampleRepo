# Program 5: Using variables and type casting
price = 3.95
widgets = 5

print("The price is", price, "for", widgets, "total widgets")
price = 3.45
print("Big sale the price is now", price)
print("The total price for all the widgets is", (price * widgets))

print("The type of price is", type(price))
print("The type of widgets is", type(widgets))

print("If prive was an int it would be", int(price))
print("If widgets was a float it would be", float(widgets))