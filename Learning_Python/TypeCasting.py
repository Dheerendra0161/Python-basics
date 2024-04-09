# TypeCasting:process of changing an entity of one data type into another

# Integer to String
num_int = 10
num_str = str(num_int)
print(num_str)  # Output: '10'

# String to Integer
str_num = "20"
num_int = int(str_num)
print(num_int)  # Output: 20

# Float to Integer
float_num = 3.14
int_num = int(float_num)
print(int_num)  # Output: 3

# String to Float
str_float = "3.14"
float_num = float(str_float)
print(float_num)  # Output: 3.14

# Convert List to Tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)
print(converted_tuple)  # Output: (1, 2, 3)

# Convert List to Set
my_list = [1, 2, 3, 2, 1]  # Contains duplicates
converted_set = set(my_list)
print(converted_set)  # Output: {1, 2, 3} - Note that set removes duplicates

# Convert Tuple to List
my_tuple = (1, 2, 5, 5, 4, 4, 9)
converted_list = tuple(my_tuple)
print(converted_list)

# Convert Tuple to Set
my_tuple = (1, 2, 5, 5, 4, 4, 9)
converted_set = set(converted_tuple)
print(converted_set)

# Convert Set to List
my_set = {1, 2, 3}
converted_list = list(my_set)
print(converted_list)  # Output: [1, 2, 3]

# Convert Set to Tuple
my_set = {1, 2, 3}
converted_tuple = tuple(my_set)
print(converted_tuple)  # Output: (1, 2, 3)

# Convert String to List
my_string = "Dheerendra"
converted_list = list(my_string)
print(converted_list)  # Output: ['H', 'e', 'l', 'l', 'o']
