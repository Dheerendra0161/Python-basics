from My_Module.custom_Module import TestData  # Import TestData class from custom_Module
# Create an instance of TestData
# test_data_instance = TestData()

# Use the instance to call the methods
# print(test_data_instance.emailTestData(461))  # Call emailTestData method with an argument
# print(test_data_instance.Data())  # Call Data method


# You can alias a module or object when importing to give it a different name.
from My_Module.custom_Module import TestData as td

test_data_instance = td()
print(test_data_instance.emailTestData(461))  # Call emailTestData method with an argument
print(test_data_instance.Data())              # Call Data method










