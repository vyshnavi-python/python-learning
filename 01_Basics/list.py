# ==========================================
# Python Lists - Complete Program
# ==========================================

# Creating Lists
numbers = [10, 20, 30, 40, 50]
names = ["Vyshnavi", "Rahul", "Anjali"]
mixed = [10, "Python", 25.5, True]

print("Numbers:", numbers)
print("Names:", names)
print("Mixed List:", mixed)

# ------------------------------------------
# Length of List
# ------------------------------------------

print("\nLength of numbers:", len(numbers))

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
print("Complete List:", numbers[:])

# ------------------------------------------
# Update List Element
# ------------------------------------------

numbers[1] = 25
print("\nUpdated List:", numbers)

# ------------------------------------------
# Append
# ------------------------------------------

numbers.append(60)
print("\nAfter append():", numbers)

# ------------------------------------------
# Insert
# ------------------------------------------

numbers.insert(2, 15)
print("After insert():", numbers)

# ------------------------------------------
# Extend
# ------------------------------------------

numbers.extend([70, 80])
print("After extend():", numbers)

# ------------------------------------------
# Remove
# ------------------------------------------

numbers.remove(25)
print("\nAfter remove():", numbers)

# ------------------------------------------
# Pop
# ------------------------------------------

numbers.pop()
print("After pop():", numbers)

numbers.pop(2)
print("After pop(2):", numbers)

# ------------------------------------------
# Delete
# ------------------------------------------

del numbers[1]
print("\nAfter del:", numbers)

# ------------------------------------------
# Sort
# ------------------------------------------

list1 = [50, 10, 30, 20, 40]

list1.sort()
print("\nAscending:", list1)

list1.sort(reverse=True)
print("Descending:", list1)

# ------------------------------------------
# Reverse
# ------------------------------------------

list1.reverse()
print("Reverse:", list1)

# ------------------------------------------
# Count
# ------------------------------------------

values = [10, 20, 10, 30, 10]

print("\nCount of 10:", values.count(10))

# ------------------------------------------
# Index
# ------------------------------------------

print("Index of 30:", values.index(30))

# ------------------------------------------
# Copy
# ------------------------------------------

copy_list = values.copy()

print("\nCopied List:", copy_list)

# ------------------------------------------
# Membership Operators
# ------------------------------------------

print("\n20 in values:", 20 in values)
print("50 not in values:", 50 not in values)

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
# List Concatenation
# ------------------------------------------

list2 = [1, 2, 3]
list3 = [4, 5, 6]

print("\nConcatenation:", list2 + list3)

# ------------------------------------------
# List Repetition
# ------------------------------------------

print("Repetition:", list2 * 3)

# ------------------------------------------
# Nested List
# ------------------------------------------

student = [
    ["Vyshnavi", 20],
    ["Rahul", 21],
    ["Anjali", 22]
]

print("\nNested List:", student)
print("First Student:", student[0])
print("First Student Name:", student[0][0])

# ------------------------------------------
# Clear
# ------------------------------------------

temp = [1, 2, 3]

temp.clear()

print("\nAfter clear():", temp)

# ------------------------------------------
# End
# ------------------------------------------

print("\nList Program Completed Successfully!")
