# Base class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id


# Intermediate class inheriting from Employee
class Engineer(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        # super() function is used to call methods and access attributes from a parent class in a multi-level inheritance
        self.specialization = specialization

    def engineer_info(self):
        print(f"Engineer {self.name} with emp ID {self.emp_id}, specializes in {self.specialization}")


# Derived class inheriting from Engineer
class SoftwareEngineer(Engineer):
    def __init__(self, name, emp_id, specialization, programming_language):
        super().__init__(name, emp_id, specialization)  # Call the parent class constructor
        self.programming_language = programming_language

    def software_engineer_info(self):
        print(
            f"Software Engineer {self.name} with emp ID {self.emp_id}, specializes in {self.specialization} and works with {self.programming_language}")


# Creating instances
engineer1 = Engineer("Nikhil", 123, "QA Engineering")
engineer1.engineer_info()  # Output: Engineer Alice with emp ID 123, specializes in Mechanical Engineering

software_engineer1 = SoftwareEngineer("Dheerendra", 456, "Software Engineering", "Python")
software_engineer1.software_engineer_info()  # Output: Software Engineer Bob with emp ID 456, specializes in Software Engineering and works with Python
