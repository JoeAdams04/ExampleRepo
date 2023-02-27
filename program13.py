# Program 13: Annual Sales
annualSales = 300000
region = 'North'
if annualSales >= 500000:
    print("Gold Customers")
elif annualSales >= 300000:
    print("Silver Customer")
    if region == "North":
        print("send a snowboard")
    else:
        print("send a baseball bat")
elif annualSales >= 100000:
    print("Bronze Customer")
print("Thank you for your businesses!")