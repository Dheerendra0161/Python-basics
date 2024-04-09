class ParentClass:
    def __init__(self, name):
        self.name = name
        print("ParentClass constructor called.")

    def parent_method(self):
        print("Parent Method")


class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # Calling Superclass Constructor
        self.age = age
        print("ChildClass constructor called.")

    def child_method(self):
        super().parent_method()  # Calling Superclass Methods
        print("Child Method")


class SecondParentClass:
    def second_parent_method(self):
        print("Second Parent Method")


class MultiLevelChild(ChildClass, SecondParentClass):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # Multiple Inheritance
        self.school = school
        print("MultiLevelChild constructor called.")

    def second_child_method(self):
        super().child_method()  # Constructor Chaining
        super().second_parent_method()


# Creating instances
print("---- Creating instances ----")
child = ChildClass("Alice", 25)
print()

print("---- Calling ChildClass methods ----")
child.child_method()
print()

print("---- Creating MultiLevelChild instance ----")
multi_child = MultiLevelChild("Bob", 30, "ABC School")
print()

print("---- Calling MultiLevelChild methods ----")
multi_child.child_method()
multi_child.second_child_method()
