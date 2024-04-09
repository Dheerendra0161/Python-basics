name = input("Enter your name:")
title = input("my title is :")
print(name + ' ' + title)

# Conversion to Integer:
age = int(input('My age is :'))
print(name + ' ' + title, age)

# Prompt the user for a decimal number
height = float(input("Enter your height (in meters): "))
print(name + ' ' + title, age, height)

# Prompt the user for a yes/no answer
answer = input("Are you a student? (yes/no): ")

# Check the answer
if answer.lower() == "yes":
    print("You are a student!")
else:
    print("You are not a student.")
