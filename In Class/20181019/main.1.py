
def calculateTax(num_product):
    product = float(input("Enter product " +str(num_product)+ " price: "))
    price = product * 1.15
    print(f"The total price of {num_product} product is ${price:.2f}.")

calculateTax("a")    