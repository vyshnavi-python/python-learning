# =====================================
# Python Operators
# =====================================

a = 10
b = 5

# -------------------------------
# 1. Arithmetic Operators
# -------------------------------
print("=== Arithmetic Operators ===")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# -------------------------------
# 2. Comparison (Relational) Operators
# -------------------------------
print("\n=== Comparison Operators ===")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# -------------------------------
# 3. Assignment Operators
# -------------------------------
print("\n=== Assignment Operators ===")

x = 10
print("Initial value:", x)

x += 5
print("x += 5 :", x)

x -= 2
print("x -= 2 :", x)

x *= 3
print("x *= 3 :", x)

x /= 2
print("x /= 2 :", x)

x //= 2
print("x //= 2 :", x)

x %= 3
print("x %= 3 :", x)

x **= 2
print("x **= 2 :", x)

# -------------------------------
# 4. Logical Operators
# -------------------------------
print("\n=== Logical Operators ===")

p = True
q = False

print("p and q :", p and q)
print("p or q  :", p or q)
print("not p   :", not p)

# -------------------------------
# 5. Bitwise Operators
# -------------------------------
print("\n=== Bitwise Operators ===")

m = 6
n = 3

print("m & n :", m & n)
print("m | n :", m | n)
print("m ^ n :", m ^ n)
print("~m    :", ~m)
print("m << 1:", m << 1)
print("m >> 1:", m >> 1)

# -------------------------------
# 6. Membership Operators
# -------------------------------
print("\n=== Membership Operators ===")

list1 = [10, 20, 30, 40]

print("20 in list1 :", 20 in list1)
print("50 in list1 :", 50 in list1)
print("20 not in list1 :", 20 not in list1)
print("50 not in list1 :", 50 not in list1)

# -------------------------------
# 7. Identity Operators
# -------------------------------
print("\n=== Identity Operators ===")

list2 = [1, 2, 3]
list3 = list2
list4 = [1, 2, 3]

print("list2 is list3 :", list2 is list3)
print("list2 is list4 :", list2 is list4)
print("list2 is not list4 :", list2 is not list4)
