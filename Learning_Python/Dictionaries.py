# Dictionary is an unordered collection of key-value pairs.
# Each key in a dictionary must be unique, and it is used to access its associated value.
# comma-separated key:value pairs inside curly braces {}.
# The keys must be immutable types (strings, numbers, or tuples), while the values can be of any data type.

Dict = {
    "name": 30,  # Key is a string
    123: "Age is 30",  # Key is an integer
    (1, 2, 3): "Tuple key",  # Key is a tuple
    True: [2, 4, 9],  # Key is a boolean
    'age': 32
}  # keys can be of different types within the same dictionary. Each key-value pair is independent of the others

# Accessing values using keys of different types:Using square brackets [] and the key.
print(Dict['name'])  # 30
print(Dict[123])  # Age is 30
print(Dict[(1, 2, 3)])  # Tuple key
print(Dict[True])  # [2, 4, 9]

# Adding and Modifying Elements:
# Adding
Dict['titile'] = 'Vishwakarma'
print(Dict)
# Modifying
Dict["age"] = 30  # Modifying an existing value
print(Dict)

# Removing Elements:remove a key-value pair using the del keyword or the pop() method.
del Dict[(1, 2, 3)]  # Deleting a key-value pair
print(Dict)  # {'name': 30, 123: 'Age is 30', True: [2, 4, 9], 'age': 30, 'titile': 'Vishwakarma'}

# Dictionary Methods:
print(Dict.keys())  # dict_keys(['name', 123, True, 'age', 'titile'])
print(Dict.values())  # dict_values([30, 'Age is 30', [2, 4, 9], 30, 'Vishwakarma'])
print(Dict.get('name'))  # 30
print(
    Dict.items())  # dict_items([('name', 30), (123, 'Age is 30'), (True, [2, 4, 9]), ('age', 30), ('titile', 'Vishwakarma')])

# Dictionary Comprehension:create dictionaries using dictionary comprehension.
Dictionary = {x: x ** 2 for x in range(5)}
print(Dictionary)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

x = [x for x in range(5)]
print(x)  # [0, 1, 2, 3, 4]

# Looping
State_Population = {
    'Mumbai': 12442373,
    'Delhi': 11007835,
    'Bangalore': 8443675,
    'Kolkata': 4631392,
    'Chennai': 4646732
}
for p, population in State_Population.items():
    print(p, population)
# items() method returns a view object that provides a list of tuples where each tuple contains a key-value pair.
