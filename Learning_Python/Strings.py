print("Delhi")
print('delhi')
print('spam eggs')
print("doesn't")
print('"Yes," they said.')

# Escaped characters \
print('"Dheerendra\'t": is a tester')
# Newline (\n)
print('First line\'s.\nSecond line.')  # First line's.
# Second line.
# Tab (\t): indentation or to separate columns of text ,space between .
print("Name:\tAlice")  # Name:   Alice
print("Age:\t30")

# Backslash (\\):single backslash is an escape character itself, so \\ is used to represent a literal backslash.
print("This is a backslash: \\")  # This is a backslash: \
print('C:\\some\\name')  # Using double backslashes to escape  #C:\some\name

# Single Quote (\') and Double Quote (\"):
# \' is used to insert a single quote character in a string that is enclosed in single quotes.
# \" is used to insert a double quote character in a string that is enclosed in double quotes.
print('It\'s a beautiful day!')  # It's a beautiful day!
print("She said, \"Hello!\"")  # She said, "Hello!"

# Raw Strings :Create raw strings by adding r or R before the quotes. Raw strings treat backslashes(\) as
# literal characters and not as escape characters.
print(r'C:\some\name')  # Using raw string with r prefix   #C:\some\name

# multiline strings :using triple quotes """ or '''
a = """
This is a
multiline
string.
"""
print(a)
b = '''
This is a
multiline
string with single quotes.
'''
print(b)

print(3 * 'num' + 'ber')  # numnumnumber

print('num''ber')  # number

fName = 'Dheerendra'

print(fName + 'Vishwakarma')  # DheerendraVishwakarma
print(fName, 'Vishwakarma')  # Dheerendra Vishwakarma

# String Slicing  : string[start:end], where start is inclusive and end is exclusive.
Name = 'Dheerendra'
print(Name[0:6])
print(Name[0:])
print(Name[:6])
print(Name[-2:])
print(Name[-3:55])
print(Name[4:42])
print(Name[42:])
print(Name[0:] + " Vishwakarma")  # Concatanation   Dheerendra Vishwakarma
print(Name[0:6] + 'ndra')  # Dheerendra

# Name[0] = 'J'# This will raise an error , once a string object is created, it cannot be modified.

Word = 'DheeredraVishwakarma@gmail.com'
print((len(Word)))  # 30

# str.format() It allows you to insert variables and expressions into strings in a readable and flexible manner
name = "Alice"
age = 30
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)

name = "Alice"
age = 30
sentence = "{0} is {1} years old. {0} lives in {2}.".format(name, age, "New York")
print(sentence)

# String function
numbers = 8750014026
name = 'Dheerendra Vishwakarma QA Engineer at Chiacon'
fullName = '   Dheerendra Vishwakarma QA Engineer at Chiacon   '
fistName = 'dheerendra'
lastName = 'Vishwakarma'
nameCount = 'Banana, Mango, Apple, Banana, Banana'

print(len(name))  # len(): Returns the length of the string.   45
print(str(numbers))  # str(): Converts an object into a string.  8750014026
print(name.lower())  # dheerendra vishwakarma qa engineer at chiacon
print(name.upper())  # DHEERENDRA VISHWAKARMA QA ENGINEER AT CHIACON
print(lastName.isupper())  # False
print(fistName.islower())  # True
print(fullName.strip())  # strip() :Removes leading and trailing whitespace from a string.
print(fullName.lstrip())  # lstrip() :removes leading whitespace
print(fullName.rstrip())  # rstrip() :removes trailing whitespace.
print(name.replace("QA", "Sr.QA"))  # Dheerendra Vishwakarma Sr.QA Engineer at Chiacon
print(nameCount.count('Banana'))  # number of occurrences of a specified substring in a string. 3

print(name.split())  # split():Splits a string into a list of substrings based on a delimiter.
# ['Dheerendra', 'Vishwakarma', 'QA', 'Engineer', 'at', 'Chiacon']


loc = "//button[contains(text(),\"Who's Driving?\")]"
print(loc)
