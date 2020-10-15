
try:
    value= 10/0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("Divide by 0")
except ValueError:
    print("Please enter a valid number")