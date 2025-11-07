# For Strings

text = "welcome to agra"
print("agra" in text)       #  True (substring found)
print("Agra" in text)       #  False (case-sensitive)
print("come" not in text)   #  False (since "come" is present)

# For Lists

cities = ["agra", "delhi", "mumbai"]
print("agra" in cities)     #  True (element present)
print("goa" not in cities)  #  True (element not present)
print("a" in cities)        #  False (not element, just part of string)

# For Tuples

numbers = (1, 2, 3, 4)
print(2 in numbers)         # True
print(5 not in numbers)     #  True


