# List: Mutable,Ordered, Duplicate, Allow indexing/slicing, [], Need to modify the collection, [1, 2, 2, 3]-->[1, 2, 2, 3, 4, 5]
# Tuple: Immutable, Ordered, Duplicate, Allow indexing/slicing, (), Need to ensure data integrity, (1, 2, 2, 3)-->(1, 2, 2, 3)
# Set: Mutable,Unordered, Not Duplicate, N  o indexing/slicing, {}, Need to check for uniqueness, {1, 2, 3}-->{1, 2, 3, 4}

list = [1, 4, 9, 16, 25]
# Accessing Elements
print(list)
print(list[1])  # 4
print(list[-1])  # 25
print(list[:])
# List Slicing
print(list[-3:])  # [9, 16, 25]

# List concatenation
print(list[-3:] + [2, 6, 4, 8])  # [9, 16, 25, 2, 6, 4, 8]

# List mutable or Modifying Elements
cube = [2, 5, 6, 8, 9, 4]
cube[1] = 15
print(cube[0:])  # [2, 15, 6, 8, 9, 4]   replaced the value 5--> 15

# Append the value of list
cube.append(14)
print(cube)

# extend()
cube.extend([2, 8, 9, 4, 6])

# Insert element at specified index
print(cube.insert(2, 74))

# Remove: Removes the first occurrence of a value.
print(cube.remove(15))  # Removes the value 15

print('**************')
# sort() :Sorts the list in ascending order.
List = [9, 5, 3, 8, 9, 4]
List.sort()
print(List)  # [3, 4, 5, 8, 9, 9]

# for costomised shorting
list = ['Dheerendra', "Vikas", 'Jitendra', 'Anil']
list.sort(key=len)
print(list)  # ['Anil', 'Vikas', 'Jitendra', 'Dheerendra']
list.reverse()  # ['Dheerendra', 'Jitendra', 'Vikas', 'Anil']
print(list)

letter = ['A', 'B', 'C', 'D', 'E']
# concat
print(letter + ['f', 'g'])
letter[2:] = 'h'
print(letter)  # ['A', 'B', 'h']
letter[1:2] = ['h', 'i', 'j', 'k']  # ['A', 'h', 'i', 'j', 'k', 'h']
print(letter)
# now remove them
letter[1:5] = []
print(letter)  # ['A', 'h']

# clear the list
letter[:] = []
print(letter)  # []
print(len(letter))
print(letter.clear())

# Nest lists (create lists containing other lists)
l1 = [1, 2, 3, 4]
l2 = [4, 5, 6, 7]
l3 = [8, 9, 10, 11]
l4 = [l1, l2, l3]
print(l4[2])  # [8, 9, 10, 11]

# List comprehension
list = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in list]
print(squared)  # Output: [1, 4, 16, 25, 36]

print('\n**********************\n')
list = [1, 2, 3, 4, 5]
my_iterator = iter(list)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
# Continue calling next() to iterate through the remaining elements
