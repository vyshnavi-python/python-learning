# ==========================================
# Python File Handling
# ==========================================

# ------------------------------------------
# Write Mode (w)
# Creates a file and writes data
# ------------------------------------------

with open("students.txt", "w") as file:
    file.write("Vyshnavi\n")
    file.write("Anjali\n")
    file.write("Rahul\n")

print("Data written successfully.")

# ------------------------------------------
# Read Mode (r)
# Reads the complete file
# ------------------------------------------

with open("students.txt", "r") as file:
    print("\nComplete File:")
    print(file.read())

# ------------------------------------------
# readline()
# Reads only one line
# ------------------------------------------

with open("students.txt", "r") as file:
    print("First Line:")
    print(file.readline())

# ------------------------------------------
# readlines()
# Returns all lines as a list
# ------------------------------------------

with open("students.txt", "r") as file:
    print("All Lines:")
    print(file.readlines())

# ------------------------------------------
# Append Mode (a)
# Adds new data without deleting old data
# ------------------------------------------

with open("students.txt", "a") as file:
    file.write("Kiran\n")

print("\nNew data appended successfully.")

# ------------------------------------------
# Read Again
# ------------------------------------------

with open("students.txt", "r") as file:
    print("\nUpdated File:")
    print(file.read())

# ------------------------------------------
# Create File (x)
# Uncomment to test
# (Run only once. Otherwise FileExistsError)
# ------------------------------------------

# with open("new_file.txt", "x") as file:
#     file.write("New file created successfully.")

# ------------------------------------------
print("\nFile Handling Program Completed Successfully!")