student = {
    "name": "Alice",
    "age": 22,
    "course": "MCA"
}

print(student["name"])   # Alice
print(student.get("age")) # 22

# Add new key-value
student["grade"] = "A"
print(student)

# Loop
for key, value in student.items():
    print(key, ":", value)
