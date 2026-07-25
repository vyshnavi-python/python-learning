# ==========================================
# Python Sets - Complete Program
# ==========================================

# Creating Sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

# ------------------------------------------
# Add()
# ------------------------------------------
set1.add(70)
print("\nAfter add(70):", set1)

# ------------------------------------------
# Update()
# ------------------------------------------
set1.update([80, 90])
print("After update([80, 90]):", set1)

# ------------------------------------------
# Remove()
# ------------------------------------------
set1.remove(90)
print("After remove(90):", set1)

# ------------------------------------------
# Discard()
# ------------------------------------------
set1.discard(100)   # No Error
print("After discard(100):", set1)

# ------------------------------------------
# Pop()
# ------------------------------------------
removed = set1.pop()
print("Removed Element:", removed)
print("After pop():", set1)

# ------------------------------------------
# Copy()
# ------------------------------------------
copy_set = set2.copy()
print("\nCopied Set:", copy_set)

# ------------------------------------------
# Union()
# ------------------------------------------
print("\nUnion:", set1.union(set2))

# Using | Operator
print("Union using | :", set1 | set2)

# ------------------------------------------
# Intersection()
# ------------------------------------------
print("\nIntersection:", set1.intersection(set2))

# Using & Operator
print("Intersection using & :", set1 & set2)

# ------------------------------------------
# Difference()
# ------------------------------------------
print("\nDifference (set1 - set2):", set1.difference(set2))

# Using - Operator
print("Difference using - :", set1 - set2)

# ------------------------------------------
# Symmetric Difference()
# ------------------------------------------
print("\nSymmetric Difference:",
      set1.symmetric_difference(set2))

# Using ^ Operator
print("Symmetric Difference using ^ :", set1 ^ set2)

# ------------------------------------------
# issubset()
# ------------------------------------------
A = {1, 2}
B = {1, 2, 3, 4}

print("\nA is subset of B:", A.issubset(B))

# ------------------------------------------
# issuperset()
# ------------------------------------------
print("B is superset of A:", B.issuperset(A))

# ------------------------------------------
# isdisjoint()
# ------------------------------------------
C = {100, 200}

print("A and C are disjoint:", A.isdisjoint(C))

# ------------------------------------------
# Membership Operators
# ------------------------------------------
print("\n20 in set1:", 20 in set1)
print("500 not in set1:", 500 not in set1)

# ------------------------------------------
# Length
# ------------------------------------------
print("\nLength of set1:", len(set1))

# ------------------------------------------
# For Loop
# ------------------------------------------
print("\nUsing for loop")

for item in set2:
    print(item)

# ------------------------------------------
# Clear()
# ------------------------------------------
temp = {1, 2, 3}

temp.clear()

print("\nAfter clear():", temp)

# ------------------------------------------
# End
# ------------------------------------------
print("\nSet Program Completed Successfully!")