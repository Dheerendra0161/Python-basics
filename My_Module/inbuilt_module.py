import math

print(math.sqrt(16))  # Output: 4.0


import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10
name = {'Dheerendra', "Vikas", 'Nikhil', 'Pranav', "Prasad"}
list_name=list(name)
print(random.choice(list_name))





import csv

# Writing to CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 25])

# Reading from CSV file
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
