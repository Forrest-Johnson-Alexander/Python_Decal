#Returns the sum of two numbers
def add (a,b):
    x = a+b
    return x
#Returns the difference of two numbers
def subtract (a,b):
    x=a-b
    return x
#Returns the product of two numbers
def multiply (a,b):
    x = a*b
    return x
#Returns the quotient of two numbers
def divide (a,b):
    if b == 0:
        print("Can't do that king")
        return
    else:
        x = a//b
        return x