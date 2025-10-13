my_set = {1, 2, 3, 3, 4}
print(my_set)   # {1, 2, 3, 4}  (duplicate removed)

# Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union → {1, 2, 3, 4, 5}
print(a & b)  # Intersection → {3}
print(a - b)  # Difference → {1, 2}
