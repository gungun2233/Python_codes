# String
s = "hello"
print(s[0])     # h

# List
lst = [1, 2, 3, "python"]
lst[0] = 10
print(lst)      # [10, 2, 3, 'python']

# Tuple
t = (1, 2, 3)
# t[0] = 10  ❌ error (cannot modify)

# Range
r = range(5)  # 0,1,2,3,4
print(list(r))
