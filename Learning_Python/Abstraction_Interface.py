# We can create interface like structure in the python but there is no as built_in 'interface' keywords in python.
from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod  # @abstractmethod is a decorator in Python that is used to declare abstract methods within abstract base classes (ABCs).
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    @abstractmethod
    def method3(self):
        pass


class A(Interface):
    def method1(self):
        print("Inside method 1")

    def method2(self):
        print("Inside method 2")

    def method3(self):
        print("Inside method 3")


obj_A = A()
obj_A.method1()  # Output: Inside method 1
obj_A.method2()  # Output: Inside method 2
obj_A.method3()  # Output: Inside method 3
