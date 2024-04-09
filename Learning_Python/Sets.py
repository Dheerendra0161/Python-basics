# List: Mutable,Ordered, Duplicate, Allow indexing/slicing, [], Need to modify the collection, [1, 2, 2, 3]-->[1, 2, 2, 3, 4, 5]
# Tuple: Immutable, Ordered, Duplicate, Allow indexing/slicing, (), Need to ensure data integrity, (1, 2, 2, 3)-->(1, 2, 2, 3)
# Set: Mutable,Unordered, Not Duplicate, No indexing/slicing, {}, Need to check for uniqueness, {1, 2, 3}-->{1, 2, 3, 4}

set = {'Dheerndra', 5, True, 3.6}
set.add('Vishwakarma')
print(set)  # Unordered each time of run {True, 'Vishwakarma', 3.6, 5, 'Dheerndra'}
set.update(['vikas', 26])
print(set)  # {True, 3.6, 5, 'Vishwakarma', 'Dheerndra', 26, 'vikas'}
set.remove('vikas')
print(set)  # {True, 3.6, 5, 'Vishwakarma', 26, 'Dheerndra'}
print(len(set))  # 6
print(3.6 in set)  # True

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
unionSet = set1.union(set2)
print(unionSet)  # Output: {1, 2, 3, 4, 5, 6}

print('\n**********************\n')
set = {'100', 'sheetala', 'Badsah', 'Nirman', 500}
my_iterator = iter(set)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# Continue calling next() to iterate through the remaining elements
