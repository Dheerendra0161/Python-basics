"""
return is for sending one value back and ending the function.
yield is for creating a generator that can produce multiple values, one at a time, while preserving its state in between pauses.
Key Differences:

Function Behavior: return terminates the function's execution and sends a single value back to the caller.
yield pauses the function's execution, remembers its state, and sends a value back to the caller.
The function can then resume execution where it left off when called again.

Number of Values: return sends back one value. yield can send back multiple values, one at a time, as needed.

State Retention: return discards the function's local variables. yield preserves the function's local variables between pauses, allowing it to pick up where it left off.
"""





def test_yield_keyword():   # like a buffet
    yield 9
    yield 5
    yield 6


yl = test_yield_keyword()
# print(next(yl))
# print(next(yl))
# print(next(yl))

#yield Keyword:
def generate_squares(start, end):
  for num in range(start, end + 1):
    yield num * num  # Pauses here, remembers state

result = generate_squares(1, 4)

# Simulate iterating over the generator (like a buffet)
for num in result:
  print(num)  # Output: 1 4 9 16

print("************************************")
#Return statement
def calculate_area(length, width):   #restaurant
  area = length * width
  return area  # Function ends here

result = calculate_area(5, 3)
print(result)  # Output: 15
