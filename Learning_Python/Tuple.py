# List: Mutable,Ordered, Duplicate, Allow indexing/slicing, [], Need to modify the collection, [1, 2, 2, 3]-->[1, 2, 2, 3, 4, 5]
# Tuple: Immutable, Ordered, Duplicate, Allow indexing/slicing, (), Need to ensure data integrity, (1, 2, 2, 3)-->(1, 2, 2, 3)
# Set: Mutable,Unordered, Not Duplicate, No indexing/slicing, {}, Need to check for uniqueness, {1, 2, 3}-->{1, 2, 3, 4}


tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('Delhi', 'Delhi', 'Mumbai', 'New York', 'Sydeney')  # Tuple allow with Duplicate value
tuple3 = (True, False, True, False)
tuple4 = (1, "hello", True, 5, "world", False, True, 'world', 3.5)

# Accessing elements by index
print(tuple4[2])
# tuple4[0] = 10   # This will raise a TypeError: 'tuple' object does not support item assignment
# print(tuple4.append('Dheerendra'))    #throw error as tuple are immutable

# Length of a tuple
print(len(tuple4))

# Iterating through a tuple
for i in tuple4:
    print(i)

# Tuple Methods
# count(): Counts the number of occurrences of a specified value.
# index(): Returns the index of the first occurrence of a specified value.

# Index of an element
print('Index of Delhi', tuple4.index("hello"))

# Count occurrences
print('Number of occurrence of world', tuple4.count("world"))
print('Number of occurrence of True', tuple4.count(True))

# Creating a new tuple by concatenating two tuples
concatTuple = tuple1 + tuple2 + tuple3 + tuple4
print(concatTuple)
print(len(concatTuple))
print(concatTuple[18])
print(concatTuple[18:])
print(concatTuple.count(True))

tuple1 = (10, 20, 30, 40, 50)
iterator = iter(tuple1)
print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30
# Continue calling next() to iterate through the remaining elements
