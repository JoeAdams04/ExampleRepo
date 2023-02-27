# Program 16: Pass Statement
annualSales = 200000
if annualSales >= 500000:
    print("Gold Customers")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000:
    pass                        # Pass keyword is merely a placeholder for something you might want to enter later. Does Nothing!
print("Thank you for your business!")