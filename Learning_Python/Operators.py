print("Dhirendra")  # Dhirendra
print(
    17 // 5)  # 3 but in actual 3.4 : // operator is used for floor division, which rounds the result down to the nearest whole number
print(50 - 30 / 2)  # 35.0
print(17 % 5)  # 2 remainder
print(2 ** 8)  # 256

a, b, c = 1, 2, 3  # Assigns values 1, 2, 3 to variables a, b, c respectively
x = y = z = 0  # Assigns the value 0 to all three variables x, y, and z

x, y = 5, 10
x, y = y, x  # Swaps the values of x and y using multiple assignment

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4  # Adds a new key-value pair to the dictionary
my_dict['b'] = 20  # Modifies the value of an existing key

x = 10
del x  # Deletes the variable x

count = 0
count += 1  # Increment count by 1, equivalent to count = count + 1
count -= 1  # Decrement count by 1, equivalent to count = count - 1

count = 0
count -= 1  # Decrement count by 1
print(count)  # Output: -1

# Equality Operator
x = 5
y = 5
print(x == y)  # Output: True
print(x == 10)  # Output: False

# Inequality Operator
x = 5
y = 10
print(x != y)  # Output: True
print(x != 5)  # Output: False

# Combining with other Operators
x = 10
y = 5
print(x > y and x != y)  # Output: True
print(x <= y)  # Output: False

# Identity Operators: Used to check if two variables point to the same object in memory.
x = [1, 2, 3]
y = [1, 2, 3]
# x and y are different objects with the same values
print(x is y)  # Output: False

a = [1, 2, 3]
b = [4, 5, 6]
# a and b are different objects with different values
print(a is not b)  # Output: True

# Membership operators allow you to check if a value is present in a sequence.
list = [1, 2, 3, 4, 5]
print(3 in list)  # True
print(3 not in list)  # False

# Check if 3 is in the list
if 3 in list:
    print("3 is in the list")
else:
    print("3 is not in the list")

# Check if 'a' is in a string
if 'a' in 'Hello':
    print("'a' is in the string")
else:
    print("'a' is not in the string")

width, height = 5, 6
print("Square is:", width * height)  # Square is: 30
print(5.3 * 8 - 5)  # 37.4
