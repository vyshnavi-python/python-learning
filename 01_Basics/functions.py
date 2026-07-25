# ==========================================
# Python Functions - Complete Program
# ==========================================

# ------------------------------------------
# Simple Function
# ------------------------------------------
def welcome():
    print("Welcome to Python!")

welcome()

# ------------------------------------------
# Function with Parameters
# ------------------------------------------
def greet(name):
    print("Hello,", name)

greet("Vyshnavi")

# ------------------------------------------
# Function with Multiple Parameters
# ------------------------------------------
def add(a, b):
    print("Sum =", a + b)

add(10, 20)

# ------------------------------------------
# Function with Return Value
# ------------------------------------------
def multiply(a, b):
    return a * b

result = multiply(5, 6)
print("Multiplication =", result)

# ------------------------------------------
# Positional Arguments
# ------------------------------------------
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Vyshnavi", 20)

# ------------------------------------------
# Keyword Arguments
# ------------------------------------------
student(age=20, name="Vyshnavi")

# ------------------------------------------
# Default Arguments
# ------------------------------------------
def country(name, place="India"):
    print(name, "is from", place)

country("Vyshnavi")
country("John", "USA")

# ------------------------------------------
# Variable Length Arguments (*args)
# ------------------------------------------
def total(*numbers):
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))

total(10, 20, 30, 40)

# ------------------------------------------
# Keyword Variable Length Arguments (**kwargs)
# ------------------------------------------
def details(**data):
    for key, value in data.items():
        print(key, ":", value)

details(name="Vyshnavi", age=20, branch="CSE")

# ------------------------------------------
# Lambda Function
# ------------------------------------------
square = lambda x: x * x

print("Square of 5 =", square(5))

# ------------------------------------------
# Recursive Function
# ------------------------------------------
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

print("Countdown:")
countdown(5)

# ------------------------------------------
# Global and Local Variables
# ------------------------------------------
college = "ABC College"   # Global Variable

def display():
    course = "Python"     # Local Variable
    print("Course:", course)

display()
print("College:", college)

# ------------------------------------------
print("\nFunctions Program Completed Successfully!")