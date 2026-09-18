def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a/b

print("====Javvis Calculator====")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
op = input("Choose Operation: ")

if op == "add":
    result = add(num1,num2)
elif op == "subtract":
    result = subtract(num1,num2)
elif op == "multiply":
    result = multiply(num1,num2)
elif op == "divide":
    result = divide(num1,num2)

print(result)
