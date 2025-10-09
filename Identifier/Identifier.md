# Identifiers, Constants, and Variables in Python

## What is an Identifier?

An identifier is a name you give to programming elements such as variables, functions, classes, modules, etc. It's basically the name you choose to refer to something in your code.

Examples of identifiers:
- `age` for a variable storing someone's age
- `calculate` for a function
- `Person` for a class

## Rules for Naming Identifiers

Python enforces strict rules for identifiers. Breaking these rules causes errors.

- Allowed Characters: Letters (A-Z, a-z), digits (0-9), and underscores (_).
- Cannot Start with a Digit: `123variable` is invalid; `variable123` is valid.
- No Keywords: Cannot use Python reserved words like `if`, `for`, `while`, `class`.
- Case-Sensitive: `age`, `Age`, and `AGE` are three different identifiers.
- No Special Symbols: Spaces, @, $, %, etc. are not allowed.

## Naming Conventions (PEP 8 Guidelines)

These guidelines improve code readability but are not enforced by Python.

- Variables & Functions: Use lowercase with underscores (snake_case).  
  Example: `user_name`, `calculate_total`
- Constants: Use all uppercase letters with underscores.  
  Example: `MAX_SPEED`, `PI`
- Classes: Use capitalized words (CamelCase).  
  Example: `Dog`, `ElectricCar`
- Meaningful Names: Always choose descriptive names.  
  Example: `number_of_students` is better than `n` or `x`.

## Reserved Words in Python

Python has a set of reserved keywords you cannot use as identifiers. You can get the full list using the `keyword` module.

Some examples:  
`False`, `None`, `True`, `and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `elif`, `else`, `for`, `if`, `import`, `return`, `while`, `with`, `yield`

## Constants in Python

Python does not have strict constants like C++ or JavaScript. Instead, we follow a naming convention to signal that a variable should be treated as a constant.

- Convention: Write the variable name in all uppercase letters with underscores.  
- Example: `PI = 3.14159`, `MAX_SPEED = 300`

Technically, you can change it, but it is considered bad practice and can confuse other programmers.

## Variables in Python

A variable is like a named container that holds data in memory. It allows you to refer to values using a simple name instead of a memory address.

- Python creates memory for the value, not the variable.
- Assigning the same value to multiple variables can reuse memory efficiently.
- Reassigning a variable updates the value, and the previous value is handled by Python's garbage collector.

### Creating a Variable

Use the assignment operator `=`:

age = 25 # assigns 25 to the variable age
name = "Alice" # assigns a string to the variable name
price = 45.95 # assigns a float to the variable price


### Characteristics of Variables

- No Declaration Needed: Python automatically determines the type.
- Dynamic Typing: A variable can hold different types over time.  
  Example:  

x = 10 # integer
x = "Hello" # string


### Using Variables

- Access and change the value stored in a variable using its name.
- Assign multiple values at once:  
`a, b, c = 10, 20, 30`
- Assign the same value to multiple variables:  
`x = y = z = 100`

Python makes it easy to work with variables while handling memory efficiently and safely.
