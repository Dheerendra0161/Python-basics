# Lambda functions are concise and allow you to define quick throwaway functions without needing to give them a name
# lambda keyword,can take any number of arguments, but can only have one expression
# Syntax      lambda arguments: expression
squre = lambda x: x ** 2
print(squre(4))  # 16

# Using lambda for a simple calculation
result = (lambda x, y: x + y)(10, 5)
print(result)  # Output: 15

# For filtering and mapping
numbers = [2, 4, 5, 6, 8, 7, 9, 10]
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)
