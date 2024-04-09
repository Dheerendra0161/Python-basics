class Loan:
    # Class variables are variables that are shared among all instances of a class.
    # They are defined within the class but outside of any methods.
    # Class variables are accessed using the class name.

    interest_rate = 0.5  # Static Variables (Class Variables)

    def __init__(self,
                 principal):  # Instance methods are functions that are defined inside a class and operate on instances of that class.
        self.principal = principal  # Instance variable

    def total_interest(self):
        return self.principal * Loan.interest_rate

    def total_amount_paid(self, debt):
        # Instance variables are variables that are unique to each instance of a class.
        # They are defined inside the __init__ method and are prefixed with self.
        # to differentiate them from class variables.
        # Instance variables hold data that is specific to each instance.

        self.debt = debt  # Instance variable
        return self.principal + self.total_interest() + self.debt


# Create two instances of the Loan class
loan1 = Loan(2000)
# We can change the class interest rate
Loan.interest_rate = 0.7
loan2 = Loan(4000)

# Calculate and print the total interest for each loan
print("Total Interest for loan1:", loan1.total_interest())
print("Total Interest for loan2:", loan2.total_interest())

# Calculate and print the total amount paid for each loan with a given debt
print("Total Amount Paid for loan1 with debt of 500:", loan1.total_amount_paid(500))
print("Total Amount Paid for loan2 with debt of 1000:", loan2.total_amount_paid(1000))


# Static Methods:Static methods are similar to class methods,
# but they don't have access to instance variables or the class itself.
class Car:
    @staticmethod
    def get_wheels():
        return 4


print(Car.get_wheels())  # Output: 4

# Instance variables are unique to each instance of a class.
# Static variables (class variables) are shared among all instances of a class.
# Instance methods operate on instances of a class and have access to instance variables through self.
# Static methods do not have access to instance variables or the class itself and are defined using @staticmetho
