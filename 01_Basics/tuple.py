# ==========================================
# Python Tuples - Complete Program
# ==========================================

# Creating Tuples
numbers = (10, 20, 30, 40, 50)
names = ("Vyshnavi", "Rahul", "Anjali")
mixed = (10, "Python", 25.5, True)

print("Numbers Tuple:", numbers)
print("Names Tuple:", names)
print("Mixed Tuple:", mixed)

# ------------------------------------------
# Length of Tuple
# ------------------------------------------

print("\nLength of Numbers Tuple:", len(numbers))

# ------------------------------------------
# Indexing
# ------------------------------------------

print("\nFirst Element:", numbers[0])
print("Last Element:", numbers[-1])

# ------------------------------------------
# Slicing
# ------------------------------------------

print("\nFirst Three Elements:", numbers[0:3])
print("Last Two Elements:", numbers[-2:])
print("Complete Tuple:", numbers[:])

# ------------------------------------------
# Tuple Concatenation
# ------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("\nConcatenation:", tuple1 + tuple2)

# ------------------------------------------
# Tuple Repetition
# ------------------------------------------

print("\nRepetition:", tuple1 * 3)

# ------------------------------------------
# Membership Operators
# ------------------------------------------

print("\n2 in tuple1:", 2 in tuple1)
print("10 not in tuple1:", 10 not in tuple1)

# ------------------------------------------
# Count Method
# ------------------------------------------

values = (10, 20, 10, 30, 10)

print("\nCount of 10:", values.count(10))

# ------------------------------------------
# Index Method
# ------------------------------------------

print("Index of 30:", values.index(30))

# ------------------------------------------
# Iterating using for loop
# ------------------------------------------

print("\nUsing for loop")

for item in values:
    print(item)

# ------------------------------------------
# Iterating using while loop
# ------------------------------------------

print("\nUsing while loop")

i = 0

while i < len(values):
    print(values[i])
    i += 1

# ------------------------------------------
# Nested Tuple
# ------------------------------------------

students = (
    ("Vyshnavi", 20),
    ("Rahul", 21),
    ("Anjali", 22)
)

print("\nNested Tuple:", students)
print("First Student:", students[0])
print("First Student Name:", students[0][0])

# ------------------------------------------
# Tuple Packing
# ------------------------------------------

student = ("Vyshnavi", 20, "CSE")

print("\nPacked Tuple:", student)

# ------------------------------------------
# Tuple Unpacking
# ------------------------------------------

name, age, branch = student

print("\nUnpacked Values")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# ------------------------------------------
# Converting Tuple to List
# ------------------------------------------

tuple_data = (100, 200, 300)

list_data = list(tuple_data)

print("\nTuple to List:", list_data)

# ------------------------------------------
# Converting List to Tuple
# ------------------------------------------

list1 = [1, 2, 3, 4]

tuple_data = tuple(list1)

print("List to Tuple:", tuple_data)

# ------------------------------------------
# Immutable Nature of Tuple
# ------------------------------------------

print("\nTuples are Immutable.")
print("Elements cannot be modified after creation.")

# Example (Don't Execute)
# numbers[0] = 100
# This will generate a TypeError.

# ------------------------------------------
# End
# ------------------------------------------

print("\nTuple Program Completed Successfully!")
