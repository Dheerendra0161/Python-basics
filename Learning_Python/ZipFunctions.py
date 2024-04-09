# The zip() function is used to combine multiple iterables (lists, tuples, etc.) element-wise into tuples.
# It creates an iterator of tuples where the i-th tuple contains the i-th element from each of the input iterables.
# If the input iterables are of different lengths, zip() stops as soon as the shortest input iterable is exhausted.


name = ["Alice", "Bob", "Charlie", "Dheerendra"]
standard = [10, 11, 12]
division = ["Fist", "Second", "Third"]

zipp = zip(name, standard, division)  # create a zip object
print(zipp)  # <zip object at 0x000002CF89E93E40>

# Zip the lists together
zipped = list(zip(name, standard, division))  # convert the zip object into a list of tuples.
print(zipped)

# Iterating through multiple sequences
for name, standard, division in zipped:
    print(f"{name} is in {standard}th standard and passed with {division}")
# The {} braces are used inside the f-string to indicate placeholders for variables.
# When the f-string(formatted string literals) is evaluated, these placeholders are replaced with the values of the corresponding variables.


# Using zip() and dict() constructor to create a dictionary
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
dictionary = dict(zip(keys, values))
print(dictionary)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
question = ['name', 'village', 'state', 'hobby']
answer = ['Dheerendra', 'Marikpur', 'Uttar Pradesh', 'Learning books']

for i, j in zip(question, answer):
    print(f'What is your {i} ?,My {i} is {j}')

my_list = [2, 3, 4, 'DK', True, 3.6]  # List is a mutable, ordered collection of elements.[]
my_set = {9, 5, 7, 'NK', True, 93.6}  # Set is an unordered collection of unique elements.{}
my_tuple = (8, 6, 6, "VK", False, 8.6)  # Tuple is an ordered and immutable collection of elements.()

# Creating zip objects
zip1 = zip(my_list, my_tuple)
zip2 = zip(my_set, my_tuple)

zip3 = zip(my_list, my_set)

zip4 = zip(my_list, my_tuple, my_set)

# Loop through unique_numbers
unique_numbers = [zip1, zip2, zip3, zip4]

for idx, zip_obj in enumerate(unique_numbers,
                              start=1):  # start=1 specifies that the index should start at 1 instead of the default 0.
    print(f"Zip {idx}:")
    for element in zip_obj:
        print(element)
    print()  # Empty line for separation
