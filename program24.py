#Program 24: Functions
def subtotal(orderAmt, salesTax = .08):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal

def orderMsg():
    print('Thank you for your order(s)')
    return

firstOrderTotal = subtotal(300, .08)
secondOrderTotal = subtotal(400, .06)

thirdOrderAmount = input("How much was the order? ")
thirdTax =input("What is your tax rate? ")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

fourthOrderTotal = subtotal(800)

print("The subtotal for the first order is %.2f" %firstOrderTotal)
print("The subtotal for the second order is %.2f" %secondOrderTotal)
print("The subtotal for the third order is %.2f" %thirdOrderTotal)
print("The subtotal for the fourth order is %.2f" %fourthOrderTotal)
orderMsg()