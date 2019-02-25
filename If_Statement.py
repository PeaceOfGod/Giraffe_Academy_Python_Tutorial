is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a Tall Male")
elif is_male and not(is_tall):
    print("You are a Short Male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(str(num1) is " greater than " + str(num2) + " and " + str(num3))
    elif num2 >= num1 and num2 >= num3:
        print(str(num2) is " greater than " + str(num1) + " and " + str(num3))
    else:
        print(str(num3) is " greater than " + str(num1) + " and " + str(num2))
max_num(17, 24, 8)