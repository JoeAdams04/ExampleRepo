# Program 7: Using indexing in Lists
regions = ["North", "South", "East", "West"]
sales = [30000, 20000, 40000, 35000]
employees = ["Alice", "Vera", "Mary", "Mel"]

print("Region:",regions[1], "\tSales: ",sales[0]) #Regions 1 is South and sales 0 is 300000
print("Region:",regions[-1], "\tSales: ",sales[-1]) #Regions -1 is West and sales -1 is 35000

employees.insert(2, "Joe") #Inserts Joe in the 2 position of the list
employees.append("Andrea") #Adds Andrea to the List of employees
employees[0] = "Logan" #Overides Alice and replaces it with Logan

for employee in employees:
    print(employee)