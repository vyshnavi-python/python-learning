# ==========================================
# Python Strings - Complete Program
# ==========================================

# Creating Strings
name = "Vyshnavi"
college = 'ABC College'

print("Name:", name)
print("College:", college)

# ------------------------------------------
# String Length
# ------------------------------------------

print("\nLength of Name:", len(name))

# ------------------------------------------
# String Indexing
# ------------------------------------------

print("\nFirst Character:", name[0])
print("Last Character:", name[-1])

# ------------------------------------------
# String Slicing
# ------------------------------------------

print("\nFirst 4 Characters:", name[0:4])
print("Last 4 Characters:", name[-4:])
print("Whole String:", name[:])

# ------------------------------------------
# String Concatenation
# ------------------------------------------

first_name = "Vyshnavi"
last_name = "M"

full_name = first_name + " " + last_name

print("\nFull Name:", full_name)

# ------------------------------------------
# String Repetition
# ------------------------------------------

print("\nPython " * 3)

# ------------------------------------------
# Membership Operators
# ------------------------------------------

print("\nIs 'V' in name?", "V" in name)
print("Is 'z' not in name?", "z" not in name)

# ------------------------------------------
# String Methods
# ------------------------------------------

text = "python programming"

print("\nOriginal:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())

# ------------------------------------------
# Replace Method
# ------------------------------------------

print("\nReplace:")
print(text.replace("python", "Java"))

# ------------------------------------------
# Find Method
# ------------------------------------------

print("\nFind 'programming':", text.find("programming"))

# ------------------------------------------
# Count Method
# ------------------------------------------

sentence = "python python java python"

print("\nCount of python:", sentence.count("python"))

# ------------------------------------------
# Startswith and Endswith
# ------------------------------------------

print("\nStarts with 'python':", text.startswith("python"))
print("Ends with 'programming':", text.endswith("programming"))

# ------------------------------------------
# Split Method
# ------------------------------------------

print("\nSplit:")
print(text.split())

# ------------------------------------------
# Join Method
# ------------------------------------------

words = ["Python", "is", "easy"]

print("\nJoin:")
print(" ".join(words))

# ------------------------------------------
# Strip Methods
# ------------------------------------------

msg = "   Hello Python   "

print("\nOriginal:", msg)
print("Strip:", msg.strip())
print("Left Strip:", msg.lstrip())
print("Right Strip:", msg.rstrip())

# ------------------------------------------
# Checking Methods
# ------------------------------------------

print("\nChecking Methods")

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("HELLO".isupper())
print("hello".islower())
print("Python Programming".istitle())

# ------------------------------------------
# Escape Characters
# ------------------------------------------

print("\nEscape Characters")

print("Hello\nPython")
print("Hello\tPython")
print("Hello \"Python\"")

# ------------------------------------------
# String Formatting
# ------------------------------------------

student = "Vyshnavi"
marks = 95

print("\nUsing format()")
print("Name: {} Marks: {}".format(student, marks))

print("\nUsing f-string")
print(f"Name: {student} Marks: {marks}")

# ------------------------------------------
# End
# ------------------------------------------

print("\nString Program Completed Successfully!")
