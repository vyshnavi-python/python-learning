# ==========================================
# Python Loops - Complete Program
# ==========================================

# ------------------------------------------
# for loop
# ------------------------------------------
print("For Loop:")

for i in range(1, 6):
    print(i)

# ------------------------------------------
# range(start, stop)
# ------------------------------------------
print("\nRange (1 to 5):")

for i in range(1, 6):
    print(i)

# ------------------------------------------
# range(start, stop, step)
# ------------------------------------------
print("\nStep Value:")

for i in range(2, 11, 2):
    print(i)

# ------------------------------------------
# Loop through a List
# ------------------------------------------
print("\nLoop through List:")

fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

# ------------------------------------------
# while loop
# ------------------------------------------
print("\nWhile Loop:")

count = 1

while count <= 5:
    print(count)
    count += 1

# ------------------------------------------
# break
# ------------------------------------------
print("\nBreak Statement:")

for i in range(1, 11):

    if i == 6:
        break

    print(i)

# ------------------------------------------
# continue
# ------------------------------------------
print("\nContinue Statement:")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

# ------------------------------------------
# pass
# ------------------------------------------
print("\nPass Statement:")

for i in range(3):
    pass

print("Pass Executed Successfully")

# ------------------------------------------
# Nested Loop
# ------------------------------------------
print("\nNested Loop:")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# ------------------------------------------
# Membership with Loop
# ------------------------------------------
print("\nLoop through String:")

name = "Vyshnavi"

for letter in name:
    print(letter)

# ------------------------------------------
print("\nLoops Program Completed Successfully!")