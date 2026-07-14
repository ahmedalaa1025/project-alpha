# Python Module 01 Notes

## Module Objective

Understand the fundamentals of Python and write clean, readable code.

---

# 1. Variables

A variable is a name that stores a value in memory.

Example:

```python
name = "Ahmed"
age = 20
gpa = 3.2
```

Rules:

- Variable names should be meaningful.
- Variable names cannot start with a number.
- Variable names are case-sensitive.

Good Examples:

```python
student_name = "Ahmed"
total_marks = 95
```

Bad Examples:

```python
x = "Ahmed"
a = 95
```

---

# 2. Data Types

Common Python data types:

- int
- float
- str
- bool

Examples:

```python
age = 20
height = 180.5
name = "Ahmed"
is_student = True
```

Check a variable type:

```python
print(type(age))
```

---

# 3. Type Conversion

Convert between data types.

Examples:

```python
age = "20"

age = int(age)

price = 15

price = float(price)

number = 100

number = str(number)
```

---

# 4. Input and Output

Input:

```python
name = input("Enter your name: ")
```

Output:

```python
print(name)
```

---

# 5. Operators

Arithmetic Operators

- +
- -
- *
- /
- //
- %
- **

Comparison Operators

- ==
- !=
- >
- <
- >=
- <=

Logical Operators

- and
- or
- not

---

# Best Practices

- Use meaningful variable names.
- Write readable code.
- Avoid unnecessary variables.
- Keep your code simple.