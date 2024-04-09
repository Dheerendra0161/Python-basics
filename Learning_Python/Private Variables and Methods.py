# Name Mangling: When you define a variable or method with double underscores
# (__private_var or __private_method), Python internally changes the name to
# include the class name. This is known as name mangling.
# double underscore naming convention (__var or __method) to indicate that a variable or method is private.

class Car:
    def __init__(self, make, model):
        self.__make = make  # Private variable
        self.__model = model  # Private variable

    def __display_info(self):  # Private method
        return f"Car: {self.__make} {self.__model}"

    def get_info(self):
        return self.__display_info()  # Accessing private method to get info

    def update_model(self, new_model):
        self.__model = new_model  # Updating private variable


# Create an instance of Car
my_car = Car("Toyota", "Camry")

# Accessing public method to get info
print(my_car.get_info())  # Output: Car: Toyota Camry

# Try to access private variables directly - This will not work and will result in an AttributeError
# print(my_car.__make)  # AttributeError
# print(my_car.__model)  # AttributeError

# Update model using public method
my_car.update_model("Corolla")

# Accessing public method to get updated info
print(my_car.get_info())  # Output: Car: Toyota Corolla
