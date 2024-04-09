# Using str.format() method or f-strings (formatted string literals)
name = "Dheerendra Vishwakarma"
age = 32
city = 'New Delhi'

# Using str.formt() method
print("Name:{},Age:{},City:{}".format(name, age, city))
print("Name:{0},Age:{1},City:{2}".format(name, age, city))
print("Name:{name},Age:{age},City:{city}".format(name=name, age=age, city=city))

# Using f-strings
# f-string. It is a way to format strings by embedding expressions inside string literals,
# using curly braces {}. The f at the beginning of the string stands for "formatted".
# It allows you to embed Python expressions directly inside a string, making string formatting much simpler and more readable.

print(f"Name: {name}, Age: {age}, City: {city}")
