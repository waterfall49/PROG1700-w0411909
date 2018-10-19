
def calculateTax(num_product):
    product = float(input("Enter product " +str(num_product)+ " price: "))
    price = product * 1.15
    print(f"The total price of {num_product} product is ${price:.2f}.")

i=1
while(i<=3):
    calculateTax(i)
    i=i+1
