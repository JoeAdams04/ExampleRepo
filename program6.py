# Program 6: Create a list
locations = ["Alaska", "Hawaii", "Iceland", "Rio"]

for location in locations:
    print(location)

print()
locations.append("Georgia")
locations.remove("Alaska")
locations.sort()

for location in locations:
    print(location)