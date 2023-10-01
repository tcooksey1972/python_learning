#A basic Calculator using Python
#Demonstration of using condition statements and math operators to build a calculator
num1 = float(input("Enter first number: "))
op = input("Enter the math operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print (num1 * num2)
else:
    print("Invalid operator")
