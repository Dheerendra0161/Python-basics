# While loop in Python
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

# Variables a and b simultaneously get the new values 0 and 1.

# To print in the same line
a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b
# 0 1 1 2 3 5 8       end=' ' allow a space between the elements instead of a newline.

print("\n*******************************\n")
count = 0
while count <= 5:
    print(count)
    count += 1
print("\n*******************************\n")

counter = 1
while True:
    print(counter)
    counter += 1
    if counter > 5:
        break  # Exit the loop if counter is greater than 5

print("\n*******************************\n")
counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue  # Skip the rest of the code for counter == 3
    print(counter)

# For loop in Python
# Iterating over a List:
# Looping Through a List
words = ["Dheerendra", 'Vishwakarma', 'Jaunpur']
for noun in words:
    print(noun + ' length', len(noun))
    # print(w + len(w))       # we can't add string and integer, but can be done by conversion using str
    print(noun + ' length', str(len(noun)))
# Looping Through a String
for char in "Dheerendra":
    print(char)

for w in words[0:2]:
    if len(w) > 5:
        print(w, len(w))
        print(w[0] + 'WISH')

# The range() function is commonly used with for loops to generate a sequence of numbers.
# Iterating over a Range
for i in range(6):
    print(i)

for i in range(5, 15):  # range(start, stop)    (inclusive of 5 but exclusive of 15).
    print(i)

for i in range(0, 16, 2):
    print(i, end=' ', )

for i in range(-10, -150, -30):
    print(i)

# iterate over the indices of a sequence
a = ['Dheerendra', 'Vikas', 'Nikhil', 'Pranav', 'Jitendra']
for i in range(len(a)):
    print(i, a[i])


print('\n***************\n')
for i in range(5):
    # Use the loop variable 'i'
    print(i)

for _ in range(5):
    # Do something 5 times without using the loop variable
    print("Hello")

print('\n***************\n')
print('******')
# Looping with Indices:You can use enumerate() to loop through a sequence and also get the index of each item.
# enumerate() to loop through both the index and the value of a list.
a = ['Dheerendra', 'Vikas', 'Nikhil', 'Pranav', 'Jitendra']
for index, i in enumerate(a):
    print(index, i)

# Tuple unpacking :Iterating Over a List of Tuples


# Nested Loops
color = ['Red', 'Blue', 'Green', 'Yellow']
fruit = ['Banana', 'Apple', 'Berry', 'Cherry']
for i in color:
    for j in fruit:
        print(i, j)

# break and continue Statements, and else Clauses on Loops
for i in range(2, 15):
    if i == 10:
        break
    print(i)

for n in range(2, 15):
    for x in range(2, n):  # range from 2 to 1.
        if n % x == 0:  # % operator is the modulo operator. It returns the remainder of the division
            print(n, 'Not')
            break
    else:
        print(n, 'is a prime number')
print('############################################')
for i in range(1, 5):
    if i % 2 == 0:
        print(i, 'is even number')
    else:
        print(i, 'is odd number')

# continue statement is used to skip the rest of the code inside the loop for
# the current iteration, and the loop moves to the next iteration.
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")

print('############################################')
x = [x for x in range(5)]
print(x)  # [0, 1, 2, 3, 4]

# If statement in Python
# If Statements
x = -62
if x < 0:
    print('\nIt\'s negative number')  # \n for printing in new line
elif x == 0:
    print("Its zero")
elif x > 0:
    print('It\'s positive number')

# Nested if and elif:
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
else:
    print("x is 5 or less")

# enumerate is a built-in Python function that allows you to loop over an iterable
# (like a list, tuple, or string) while also keeping track of the index of each item.
# It returns an enumerate object, which can be used to get the index and value of each item in the iterable.

fruits = ['apple', 'banana', 'cherry', 'date']

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print("\n.............................\n")
fruits = ['apple', 'banana', 'cherry']
prices = [1.0, 0.5, 1.2]

for index, (fruit, price) in enumerate(zip(fruits, prices)):
    print(f"Item {index}: {fruit} - ${price}")
