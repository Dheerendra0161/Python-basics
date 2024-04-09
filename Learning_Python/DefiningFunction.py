# Defining Functions :creating reusable blocks of code that perform specific tasks.
def addNumbers(a, b):  # parameters are optional input variables that the function can take.
    result = a + b
    return result


sumResult = addNumbers(5, 6)
print(sumResult)


def greet(name):
    print("Hello: ", name)


# Calling the function
greet("Dheerendra")


# Default Arguments: If a parameter is not provided when calling the function, the default value will be used.
def greet1(name, message='Hello'):  # default arguments ('Hello') should be defined after non-default arguments
    print(name, message)


greet1('Dheerendra')  # Dheerendra Hello

# Mixing Default and Keyword Arguments:If a parameter is  provided when calling the function, the parameter value will be used.
greet1("dherendra", 'Go to home')  # dherendra Go to home


# Keyword Arguments
def greet2(message, name):
    print(message + ' sended to ' + name)


greet2('Prompt', 'Dheerendra')


def greet3(message, name):
    return f"{message}{name}"


print(greet3("Great", " Chiacon"))


# Returning Multiple Values:A function can return multiple values as a tuple.
def StudentInfo(name, age, grade):
    return name, age, grade


# Calling the function and unpacking the returned tuple
studentName, studentAge, studentArade = StudentInfo("Dheerendra", 25, "A")
print("Student Name:", studentName)
print("Student Age:", studentAge)
print("Student Grade:", studentArade)


# Function Scope:


# Variable Number of Arguments
def sumAllValue(*args):
    total = sum(args)
    return total


print(sumAllValue(1, 5, 9))


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


fib(10)


def fibonacci(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f = fibonacci(150)
print(f)


# Scope of the Variables
# Local Scope (Function Scope):
def my_function():
    x = 10  # Local variable
    print("Inside function:", x)


my_function()


# Enclosing Scope (Nested Function Scope):
def outer_function():
    x = 10
    print("Outside inner function:", x)

    def inner_function():
        print("Inside inner function:", x)

    inner_function()


outer_function()

# Global Scope (Module Scope):Accessible from anywhere within the module
x = 10  # Global variable


def my_function():
    print("Inside function:", x)


my_function()
print("Outside function:", x)


def modify_global():
    global x
    x = 20


modify_global()
print("After modification:", x)

# Built-in Scope:Variables pre-defined in Python.Accessible from anywhere in the code.
x = 10  # Global variable


def outer_function():
    y = 20  # Enclosing (Outer) variable

    def inner_function():
        z = 30  # Local variable
        print("Inside inner function:", x, y, z)

    inner_function()
    print("Inside outer function:", x, y)  # x and y are accessible here


outer_function()
print("Outside function:", x)  # x is accessible here


# Trying to modify global variable from a function
def try_modify_global():
    global x
    x += 5  # or x=x+15


try_modify_global()
print("After modification:", x)  # x is modified to 15

"""
Local Scope: Inside functions, only accessible within that function.
Enclosing Scope: Inside nested functions, accessible from the enclosing (outer) function.
Global Scope: At the top-level of a module, accessible throughout the module.
Built-in Scope: Pre-defined names in Python, accessible everywhere."""
print('############################################')
