print("Arockiya's Calculator")
#  By default, all the inputs are considered strings
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator:")

if op == "+":
    result = num1+num2
elif op == "-":
    result = num1-num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1/num2
else:
    result = 0
    print("Invalid operator")

# result = float(num1)+float(num2)
print("The result is: "+ str(result))
