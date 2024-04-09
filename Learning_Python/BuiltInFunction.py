# Basic Functions:
print("Hello, World!")

# input(prompt): Read a string from standard input.
# user_input = input("Enter your name: ")

# len(iterable): Return the length (number of items) of an object
numbers = [1, 2, 3, 4, 5]
print("Number of elements:", len(numbers))

# type(object): Return the type of an object.
number = 10
print("Type of number:", type(number))

# Type Conversion:
# int(x), float(x), str(x): Convert x to an integer, float, or string, respectively.
num_str = "10"
num_int = int(num_str)

# bool(x): Convert x to a Boolean (True or False)
result = bool(0)  # False

# list(iterable), tuple(iterable): Convert an iterable to a list or tuple.
numbers_tuple = (1, 2, 3)
numbers_list = list(numbers_tuple)  # [1, 2, 3]
print(tuple(numbers_list))  # (1, 2, 3)

# Math Functions:
# max(iterable), min(iterable): Return the maximum or minimum value in an iterable.
numbersList = [5, 2, 8, 1]
maxValue = max(numbersList)
minValue = min(numbersList)
print(maxValue, minValue)

# sum(iterable): Return the sum of all elements in an iterable.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # 15

# File Handling: See File of project
