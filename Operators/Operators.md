# Python Operators

Operators are **symbols** that perform specific operations on variables and values.

---

## Types of Operators in Python

Python provides several types of operators:

1. Arithmetic Operators  
2. Assignment Operators  
3. Comparison Operators  
4. Logical Operators  
5. Identity Operators  
6. Membership Operators  


---

## 1. Arithmetic Operators

Used to perform **mathematical operations**.

| Operator | Description        | Example | Output |
|----------|------------------|---------|--------|
| `+`      | Addition          | `5 + 3` | 8      |
| `-`      | Subtraction       | `5 - 3` | 2      |
| `*`      | Multiplication    | `5 * 3` | 15     |
| `/`      | Division          | `5 / 2` | 2.5    |
| `//`     | Floor Division    | `5 // 2`| 2      |
| `%`      | Modulus (Remainder)| `5 % 2`| 1      |
| `**`     | Exponentiation    | `2 ** 3`| 8      |

---

## 2. Assignment Operators

Used to **assign values** to variables or **update them** based on arithmetic operations.

| Operator | Example   | Equivalent To |
|----------|----------|----------------|
| `=`      | `x = 5`  | Assign value 5 |
| `+=`     | `x += 3` | `x = x + 3`   |
| `-=`     | `x -= 3` | `x = x - 3`   |
| `*=`     | `x *= 3` | `x = x * 3`   |
| `/=`     | `x /= 3` | `x = x / 3`   |
| `%=`     | `x %= 3` | `x = x % 3`   |
| `**=`    | `x **= 2`| `x = x ** 2`  |
| `//=`    | `x //= 2`| `x = x // 2`  |

---

## 3. Comparison Operators

Used to **compare two values**. They return `True` or `False`.

| Operator | Description                 | Example   | Output |
|----------|----------------------------|-----------|--------|
| `==`     | Equal to                    | `5 == 3`  | False  |
| `!=`     | Not equal to                | `5 != 3`  | True   |
| `>`      | Greater than                | `5 > 3`   | True   |
| `<`      | Less than                   | `5 < 3`   | False  |
| `>=`     | Greater than or equal to    | `5 >= 3`  | True   |
| `<=`     | Less than or equal to       | `5 <= 3`  | False  |

---

## 4. Logical Operators

Used to **combine multiple conditions**.

| Operator | Description                         | Example             | Output |
|----------|-----------------------------------|-------------------|--------|
| `and`    | True if both conditions are True  | `x > 3 and x < 10` | True   |
| `or`     | True if at least one condition is True | `x > 3 or x < 4` | True   |
| `not`    | Reverses the result               | `not(x > 3 and x < 10)` | False |

### Truth Tables

**AND Operator**

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

**OR Operator**

| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

**NOT Operator**

| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

---

## 5. Identity Operators

Used to compare **memory locations of two objects** (not their values).

| Operator   | Description                      | Example | Output       |
|------------|---------------------------------|---------|-------------|
| `is`       | True if both refer to same object | `x is y` | True / False |
| `is not`   | True if not the same object       | `x is not y` | True / False |

---

## 6. Membership Operators

Used to check whether a **value exists in a sequence** (string, list, tuple, set, dictionary).

| Operator | Description                  | Example         | Output |
|----------|------------------------------|----------------|--------|
| `in`     | True if value exists          | `'a' in 'apple'` | True  |
| `not in` | True if value does not exist  | `'b' not in 'apple'` | True |





