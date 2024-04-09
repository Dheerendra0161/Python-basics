# Abstraction: Refers to the concept of hiding the complex implementation details while providing a simple
# interface to the users.

# We cannot create an object of an abstract class in Python
# They are meant to be subclassed, and their main purpose is to define a common interface for its subclasses.
# Abstract classes cannot be instantiated on their own because they typically contain one or more abstract
# methods that do not have an implementation in the abstract class.

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    def method3(self):
        print('Inside method 3')


class B(A):
    def method1(self):
        print("Inside method 1")


# obj_B = B()           # Can't instantiate abstract class B without an implementation for abstract method 'method2'
# obj_B.method1()
# obj_B.method2()
# obj_B.method3()


class C(B):
    def method2(self):
        print("Inside method 2")


obj_C = C()
obj_C.method1()  # Output: Inside method 1 (inherited from B)
obj_C.method2()  # Output: Inside method 2 (defined in C)
obj_C.method3()  # Output: Inside method 3 (inherited from A)
