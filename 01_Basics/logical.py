# ==========================================
# Python If-Else Statements
# ==========================================

# Simple if
age = 20

if age >= 18:
    print("Eligible to Vote")

# ------------------------------------------

# if-else
marks = 30

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# ------------------------------------------

# if-elif-else
score = 85

if score >= 90:
    print("Grade A+")
elif score >= 75:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Fail")

# ------------------------------------------

# Nested if
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Not Eligible")

# ------------------------------------------

# Logical Operators
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Login")

# ------------------------------------------

# Short Hand if
number = 10

if number > 5:
    print("Greater than 5")

# ------------------------------------------

# Ternary Operator
age = 16

print("Eligible") if age >= 18 else print("Not Eligible")

# ------------------------------------------

# Comparison Operators
a = 15
b = 20

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# ------------------------------------------

print("\nIf-Else Program Completed Successfully!")