# Example of Identity Operators and memory locations

# Both variables are integers
a = 10   # Suppose memory location of 10 is 12411
b = 10   # Memory location of 10 is same as a, because integers are immutable and shared in Python

print(a is b)   # True, because both point to the same memory location (same object)
print(a == b)   # True, values are equal

# Now b is a string
b = "10"  # Different data type, stored at a different memory location, suppose 13455

print(a is b)   # False, because a (int) and b (str) are different objects
print(a == b)   # False, values are different as well
