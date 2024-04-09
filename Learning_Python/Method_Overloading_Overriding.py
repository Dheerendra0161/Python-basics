class Calculator:
    def add(self, a, b, c=None):

        if c is None:
            return a + b
        else:
            return a + b + c


# Test method overloading
calc = Calculator()
print("Sum (2 arguments):", calc.add(10, 20))  # Output: Sum (2 arguments): 30
print("Sum (3 arguments):", calc.add(10, 20, 30))


class Company:

    def employee(self):
        print("IT department")

# Python does not support method overloading by default based on different signatures.
#     def employee(self, emp_id):
#         print("Employee ID:", emp_id)
#         print("IT department")


class QA_Department(Company):
    def employee(self):
        print("QA department")


class Azure_Department(Company):
    def employee(self):
        print("Azure department")


# Test method overriding
azure = Azure_Department()
azure.employee()

QA = QA_Department()
QA.employee()
