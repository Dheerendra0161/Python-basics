class Organisation:
    def __init__(self, empName, empId, empJobTitle):
        self.empName = empName
        self.empId = empId
        self.empJobTitle = empJobTitle

    def client(self, clientName):
        self.clientName = clientName
        print(f"{self.empName} with empID {self.empId} is working as {self.empJobTitle} for {self.clientName}")

    def project(self, projectName):
        self.projectName = projectName
        print(
            f"{self.empName} with empID {self.empId} is working as {self.empJobTitle} for {self.clientName} on {self.projectName}")


class BillableAmount:
    def billing(self, salary):
        self.salary = salary
        print(f"{self.empName} salary amount Rs.{self.salary} is reimbursed for {self.projectName}")


class Management:
    def hierarchy(self):
        print('Follow hierarchical structure')


class Joiner(Organisation, BillableAmount, Management):
    pass


j1 = Joiner("Dheerendra", 123, "QA Engineer")
j1.client('Chiacon')
j1.project('Dabur')
j1.billing(541236)


class A:
    def method(self):
        print("Method from A")


# Same method name
class B(A):
    def method(self):
        print("Method from B")


class C(A):
    def method(self):
        print("Method from C")


class D(B, C):
    pass


# MRO for D
print(D.__mro__)

# Method resolution order(MRO): determines the order in which methods are searched for and executed in a class hierarchy,
# especially in the context of multiple inheritance.

# The MRO in Python does follow a depth-first, left-right search, but it considers the entire inheritance graph.
# It ensures that each class is visited only once during the search process, maintaining consistency and resolving conflicts.
# The C3 linearization algorithm is used to calculate the MRO, preserving the order of inheritance and providing a predictable search path.
# Understanding MRO is crucial for proper method resolution, especially in cases of multiple inheritance and method overriding.
