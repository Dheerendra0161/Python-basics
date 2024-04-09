# A module in Python is a file containing Python definitions and statements.
# A module can define functions, classes, and variables. Modules can also
# include runnable code. Grouping related code into a module makes the code
# easier to understand and use. It also makes the code logically organized.
import datetime

import math  # importing the entire math module into your script's
from math import *  # is another form of import that imports all functions and constants
from math import factorial  # importing only the factorial function from the math module directly


class TestData:
    def Data(self):
        return datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S-%f")

    def emailTestData(self, enterValue):
        return f'dheerendra{enterValue}@gmail.com'
