# Encapsulation in Python refers to bundling data (attributes)
# and methods (functions) that operate on the data within a class.
# It hides the internal state of an object and restricts direct access from outside the class.
# This helps in data protection, ensuring that data is accessed and modified only through the
# class's public interface, enhancing code organization and security.

class Person:
    # def __init__(self, name, age):
    #     self._name = name
    #     self._age = age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age must be a positive integer")
        self._age = age

    def get_age(self):
        return self._age


# person = Person("Dheerendra", 32)

person = Person()
person.set_name('Nikhil')  # Set the name to John
person.set_age(25)  # Set the age to 25

print("Name is :", person.get_name())
print("Age is :", person.get_age())
