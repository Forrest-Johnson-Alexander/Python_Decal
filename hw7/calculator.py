#I'm having trouble running the module. I have everything in the right places and I'm calling it correctly, but it's just not running correctly. While I built the code, as I called the module it responded with the functions under the module, but it just won't call. 
while True:
    import math_tools as mt
    Continue = int(input("Continue?(1:Yes|2:No): "))
    if Continue == 1:
        num1 = int(input("enter a number: "))
    num2 = int(input("enter a second number: "))
    operation = int(input("Enter which operation you would like to perform(1:addition|2:subtraction|3:multiplication|4:division): "))
    if operation == 1:
        Sum = mt.add(num1,num2)
        print(Sum)
    if operation == 2:
        Difference = mt.subtract(num1,num2)
        print(Difference)
    if operation == 3:
        Product = mt.multiply(num1,num2)
        print(Product)
    if operation == 4:
        Quotient = mt.divide(num1,num2)
        print(Quotient)
    else:
        break