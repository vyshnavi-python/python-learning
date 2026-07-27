# ==========================================
# Python Exception Handling
# ==========================================

# ------------------------------------------
# ZeroDivisionError
# ------------------------------------------
try:
    print("Example 1: ZeroDivisionError")
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# ------------------------------------------
# ValueError
# ------------------------------------------
try:
    print("\nExample 2: ValueError")
    age = int("Hello")

except ValueError:
    print("Invalid input. Please enter a number.")

# ------------------------------------------
# IndexError
# ------------------------------------------
try:
    print("\nExample 3: IndexError")
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Index out of range.")

# ------------------------------------------
# NameError
# ------------------------------------------
try:
    print("\nExample 4: NameError")
    print(name)

except NameError:
    print("Variable is not defined.")

# ------------------------------------------
# else Block
# ------------------------------------------
try:
    print("\nExample 5: else Block")
    result = 20 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Division Successful:", result)

# ------------------------------------------
# finally Block
# ------------------------------------------
try:
    print("\nExample 6: finally Block")
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program Finished")

# ------------------------------------------
# raise Keyword
# ------------------------------------------
try:
    print("\nExample 7: raise Keyword")

    age = 15

    if age < 18:
        raise Exception("You are not eligible to vote.")

except Exception as e:
    print(e)

# ------------------------------------------
# Multiple Exceptions
# ------------------------------------------
try:
    print("\nExample 8: Multiple Exceptions")

    number = int(input("Enter a number: "))
    print(10 / number)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

# ------------------------------------------
print("\nException Handling Program Completed Successfully!")