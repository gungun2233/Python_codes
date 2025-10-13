x = None
print(x)        # None
print(type(x))  # <class 'NoneType'>

# Example: function returning nothing
def greet():
    print("Hello!")

result = greet()
print(result)   # None (since no return statement)
