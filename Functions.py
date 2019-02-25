def say_hi():
    name = input("Enter your name: ")
    print("Hi " + name)

# say_hi()

# array = [1, 2, 3, 4, 5]
# for i in array:
#    print(array[i])
# Get the Maximum of the list of integers
# def maximum():
#    num = [1, 2, 10, 50, 94, 75, 81, 15]

#   for i in num:
#        j = i + 1
#       for j in num:
#            if (num[i] > num[j]):
#                temp = num[j]
#                num[j] = num[i]
#                num[i] = temp
#            continue
#    print(num[i])
# maximum()
# Function with Arguments
def character(name, age):
    # name = input("Enter your name: ")
    # age = int(input("Enter your age: "))
    print("Hello " + name + ", you are " + str(age) + " years old")
character("Mike", 30)
character("Peace", 23)