# Boolean Operations
x = True
y = False
print(x and y)  # and: Returns True if both operands are True.
print(x or y)  # or: Returns True if at least one operand is True.

# Comparison Operators
a = 10
b = 5
print(a > b)  # True
print(a <= b)  # False
print(a == b)  # False

# Boolean in Control Structures
age = 17
if age >= 18:
    print("You are adult")
else:
    print("You are minor")

# Boolean Conversion   : other types can be converted to boolean using the bool() function.
# Empty objects or zero values are considered False
emptyList = []
List = [1, 2, 5, 6, 8]
print(bool(emptyList))  # False
print(bool(list))  # True
ZeroValue = 0
NonZero = 15
print(bool(ZeroValue))  # False
print(bool(NonZero))  # True
