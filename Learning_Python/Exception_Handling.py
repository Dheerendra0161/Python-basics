'''
#Basic Syntax:
try:
    # Code that may raise an exception
    # If an exception occurs here, the execution will jump to the except block
    # Otherwise, this code will run without interruption
    # It's good to keep the minimal code that might raise an exception inside the try block
except SomeException:
    # Code to handle the exception
    # If a SomeException occurs in the try block, this code will run
    # You can have multiple except blocks to handle different types of exceptions
    # If no exception of this type occurs, this block will be skipped
except AnotherException as e:
    # You can also catch the exception object for further analysis
    # 'e' is the exception object, you can access its attributes for details
    # This block will handle AnotherException
    # If no exception of this type occurs, this block will be skipped
else:
    # Optional block, runs if no exception occurs
    # This block is executed if the try block does not raise an exception
finally:
    # finally block will always execute, whether an exception occurred or not.
    # Optional block, runs whether an exception occurs or not
    # Useful for cleanup code, closing files, etc.



#Handling Multiple Exceptions:
try:
    # Some code that may raise exceptions
except (Exception1, Exception2, Exception3) as e:
    # Handle multiple exceptions
    # 'e' will contain the exception object



#Raising Exceptions:
#You can also raise exceptions explicitly with the raise statement:
raise ValueError("Invalid input")


'''


def divide_number(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError as e:
        print(f"Error: {e}")
    else:
        print("Division successful. Result:", result)
    finally:
        print("Always executed")


def raise_customised_exception(num):
    try:
        if num < 0:
            raise ValueError("Number cannot be negative.")
        elif num == 0:
            raise Exception("Number is zero.")
        else:
            print("Number is valid")

    except ValueError as e:
        print(f"ValueError: {e}")

    except Exception as e:
        print(f"Exception: {e}")
    else:
        print("No exceptions raised.")


def main():
    # Example 1: Handling division by zero
    print("Example 1:")
    divide_number(10, 2)  # Normal division
    divide_number(10, 0)  # Division by zero
    divide_number("10", 2)  # Type error

    print("\n-----------------\n")

    # Example 2: Raising custom exceptions
    print("Example 2:")
    raise_customised_exception(5)  # Valid number
    raise_customised_exception(-5)  # Negative number
    raise_customised_exception(0)  # Zero


if __name__ == "__main__":
    main()

# The line if __name__ == "__main__": allows you to define a block of code that
# should only run when the script is executed directly, not when it is imported as
# a module. This is commonly used to define the main functionality of a script.
# If the file is imported as a module into another script, then __name__ is set to the name of the module.
# executed directly, not when it is imported as a module.
