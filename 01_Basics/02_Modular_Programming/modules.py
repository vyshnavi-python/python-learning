# ==========================================
# Python Modules
# ==========================================

# Importing Entire Module
import math

print("Square Root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Value of PI:", math.pi)
print("Ceil Value:", math.ceil(4.2))
print("Floor Value:", math.floor(4.8))

# ------------------------------------------

# Import Specific Function
from math import sqrt

print("\nSquare Root of 64:", sqrt(64))

# ------------------------------------------

# Alias
import math as m

print("\nPI Value using Alias:", m.pi)

# ------------------------------------------

# Random Module
import random

print("\nRandom Number:", random.randint(1, 10))
print("Random Choice:", random.choice(["Apple", "Mango", "Orange"]))

# ------------------------------------------

# Datetime Module
import datetime

today = datetime.datetime.now()

print("\nCurrent Date and Time:")
print(today)

# ------------------------------------------

print("\nModules Program Completed Successfully!")