is_male = False

if not is_male:
    print("You are a male")
else:
    print("You are not male")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(7,8,9))