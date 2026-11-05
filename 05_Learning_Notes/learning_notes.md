# 📚 Learning Notes — Introduction to AI & Python

> Comprehensive notes covering all five module objectives.  
> Suitable for a complete beginner who has never programmed before.

---

## MODULE 1: Introduction to Artificial Intelligence

### 1.1 What is Artificial Intelligence?

**Definition:**  
Artificial Intelligence (AI) is the science of programming computers to perform tasks that normally require human intelligence — such as understanding language, recognising images, making decisions, and learning from experience.

**Simple Analogy:**  
Think of how you learned to recognise a dog. You saw hundreds of dogs over the years. Your brain built a pattern. Now when you see a new dog you've never seen before, you instantly know it's a dog. AI works the same way — it learns from examples.

**Key Characteristics of AI:**
- Learns from data or experience
- Makes decisions or predictions
- Can improve over time
- Handles complex, unpredictable inputs

**Examples you already use:**
| Application | AI in action |
|-------------|-------------|
| Gmail | Filters spam automatically |
| YouTube | Recommends videos you might like |
| Google Maps | Predicts traffic and reroutes |
| Phone keyboard | Autocorrects and predicts your next word |
| Face Unlock | Recognises your face in different lighting |

---

### 1.2 Types of AI

| Type | Exists Today? | Description | Example |
|------|---------------|-------------|---------|
| **Narrow AI** | YES | Does one specific task very well | Chess engine, face recognition |
| **General AI** | NO (yet) | Can do anything a human can | Science fiction concept |
| **Super AI** | NO | Surpasses human intelligence in all areas | Theoretical only |

> All AI that exists today is **Narrow AI**.

---

### 1.3 AI vs Machine Learning vs Deep Learning

```
┌─────────────────────────────────────┐
│          ARTIFICIAL INTELLIGENCE    │
│  "Make machines act intelligently"  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │       MACHINE LEARNING        │  │
│  │  "Learn patterns from data"   │  │
│  │                               │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │      DEEP LEARNING      │  │  │
│  │  │  "Neural networks with  │  │  │
│  │  │   many layers"          │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

**Remember:**
- ML is a **subset** of AI
- DL is a **subset** of ML
- Every DL system is ML; every ML system is AI — but not the reverse

---

### 1.4 Types of Machine Learning

#### Supervised Learning
- **Data:** Labelled (every example has a correct answer)
- **Goal:** Learn to predict the label for new data
- **Analogy:** Studying with an answer key
- **Examples:** Spam detection, house price prediction, disease diagnosis

#### Unsupervised Learning
- **Data:** Unlabelled (no correct answers provided)
- **Goal:** Find hidden patterns or groupings
- **Analogy:** Sorting a pile of objects by shape without being told the categories
- **Examples:** Customer segmentation, anomaly detection, topic modelling

#### Reinforcement Learning
- **Data:** No dataset — learns through trial and error
- **Goal:** Maximise reward by choosing the best actions
- **Analogy:** Training a dog with treats
- **Examples:** Game-playing AI (Chess, Go), robotics, self-driving cars

---

### 1.5 Advantages and Limitations of AI

**Advantages:**
- Processes information millions of times faster than humans
- Works 24/7 without fatigue
- Makes fewer errors on repetitive tasks
- Finds hidden patterns in massive datasets
- Personalises experiences for each user

**Limitations:**
- Needs huge amounts of data to learn
- Can inherit and amplify human biases
- Cannot truly reason, understand context, or feel emotions
- Many AI decisions are impossible to explain ("black box")
- Expensive to develop and run
- May displace certain types of jobs

---

### 1.6 Practice Questions — AI Theory

1. What is the difference between Narrow AI and General AI?
2. Give three examples of AI you use in daily life.
3. What is the key difference between supervised and unsupervised learning?
4. Why is Deep Learning considered powerful for images and speech?
5. Name two advantages and two limitations of AI.
6. What does "Reinforcement Learning" mean? Give an analogy.

**Key Takeaway:** AI is already part of everyday life. Understanding it helps you use it wisely and participate in its development.

---

---

## MODULE 2: Python Fundamentals

### 2.1 What is Python?

Python is a high-level, general-purpose programming language designed to be readable and beginner-friendly. Created by Guido van Rossum in 1991, it is now one of the most popular languages in the world — used in web development, data science, AI, automation, and more.

**Why Python for AI?**
- Simple syntax — reads almost like English
- Huge library ecosystem (NumPy, Pandas, TensorFlow, etc.)
- Strong community and learning resources
- Industry standard for data science and machine learning

---

### 2.2 Variables and Data Types

A **variable** is a named container that stores a value.

```python
# Declaring variables
name    = "Alice"      # str  — text in quotes
age     = 20           # int  — whole number
height  = 5.7          # float — decimal number
is_pass = True         # bool — True or False
```

| Type | Full Name | Example | Use Case |
|------|-----------|---------|----------|
| `int` | Integer | `42`, `-7`, `0` | Age, count, year |
| `float` | Floating point | `3.14`, `-0.5` | Price, temperature |
| `str` | String | `"Hello"`, `'AI'` | Names, messages |
| `bool` | Boolean | `True`, `False` | Yes/No conditions |

**Checking the type:**
```python
x = 3.14
print(type(x))   # Output: <class 'float'>
```

**Type conversion:**
```python
age_str = "25"
age_int = int(age_str)   # "25" -> 25
price   = float("9.99")  # "9.99" -> 9.99
label   = str(100)       # 100 -> "100"
```

**Expected output:**
```
<class 'float'>
```

---

### 2.3 Operators

**Arithmetic operators:**
```python
a, b = 15, 4
print(a + b)   # 19  — addition
print(a - b)   # 11  — subtraction
print(a * b)   # 60  — multiplication
print(a / b)   # 3.75 — division (always float)
print(a // b)  # 3   — floor division (drops decimal)
print(a % b)   # 3   — modulo (remainder)
print(a ** 2)  # 225 — exponent (15 squared)
```

**Comparison operators (always return True/False):**
```python
print(10 == 10)  # True
print(10 != 5)   # True
print(10 > 20)   # False
print(10 <= 10)  # True
```

**Logical operators:**
```python
age, has_id = 20, True
print(age >= 18 and has_id)   # True — both must be True
print(age < 18 or has_id)     # True — at least one True
print(not has_id)             # False — flips True to False
```

**Important modulo uses:**
```python
# Check even/odd
print(7 % 2)   # 1 -> Odd
print(8 % 2)   # 0 -> Even

# Check leap year
print(2024 % 4)  # 0 -> Leap year
```

---

### 2.4 Conditional Statements

**Syntax:**
```python
if condition:
    # runs if condition is True
elif another_condition:
    # runs if first was False, this is True
else:
    # runs if all conditions above were False
```

**Example — Grade assignment:**
```python
percentage = 82

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

**Expected output:**
```
Grade: A
```

**One-line if (ternary):**
```python
result = "PASS" if percentage >= 50 else "FAIL"
print(result)   # PASS
```

---

### 2.5 For Loops

```python
# Loop a fixed number of times
for i in range(5):
    print(i)        # prints 0, 1, 2, 3, 4

# Loop over a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**Expected output:**
```
0
1
2
3
4
Apple
Banana
Cherry
1. Apple
2. Banana
3. Cherry
```

**range() cheat sheet:**
```python
range(5)       # 0, 1, 2, 3, 4
range(1, 6)    # 1, 2, 3, 4, 5
range(0,10,2)  # 0, 2, 4, 6, 8   (step of 2)
range(10,0,-1) # 10,9,8,...,1     (count down)
```

---

### 2.6 While Loops

```python
counter = 1
while counter <= 5:
    print(f"Count: {counter}")
    counter += 1    # MUST update — otherwise infinite loop!
```

**Expected output:**
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

**break and continue:**
```python
for n in range(1, 11):
    if n == 5:
        break       # stop the loop entirely
    print(n)        # prints 1, 2, 3, 4

for n in range(1, 6):
    if n == 3:
        continue    # skip this iteration
    print(n)        # prints 1, 2, 4, 5
```

---

### 2.7 Lists

```python
marks = [88, 72, 95, 60, 45]

# Access
print(marks[0])    # 88  (first item)
print(marks[-1])   # 45  (last item)

# Modify
marks[2] = 98      # change index 2

# Methods
marks.append(77)   # add to end
marks.sort()       # sort ascending
marks.reverse()    # reverse in place

# Useful functions
print(len(marks))   # number of items
print(max(marks))   # largest value
print(min(marks))   # smallest value
print(sum(marks))   # total of all values
```

**List slicing:**
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [50, 40, 30, 20, 10]
```

---

### 2.8 Tuples

```python
coordinates = (28.61, 77.20)   # parentheses, not square brackets
print(coordinates[0])           # 28.61

# Tuples are IMMUTABLE — cannot change after creation
# coordinates[0] = 10   ← This would raise TypeError!

# Tuple unpacking
lat, lon = coordinates
print(f"Lat: {lat}, Lon: {lon}")
```

**When to use tuples vs lists:**
- List: data that changes (shopping cart, student marks)
- Tuple: data that is fixed (GPS coordinates, RGB colours, days of week)

---

### 2.9 Dictionaries

```python
student = {
    "name"  : "Alice",
    "age"   : 20,
    "grade" : "A"
}

# Access
print(student["name"])           # Alice
print(student.get("phone", "N/A"))  # N/A (key doesn't exist)

# Add / update
student["email"] = "alice@example.com"
student["age"]   = 21

# Loop
for key, value in student.items():
    print(f"{key}: {value}")

# Check key exists
print("name" in student)   # True
print("phone" in student)  # False
```

**Expected output:**
```
Alice
N/A
name: Alice
age: 21
grade: A
email: alice@example.com
True
False
```

---

### 2.10 Functions

```python
# Define a function
def calculate_grade(percentage):
    """Return grade string based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 50:
        return "Pass"
    else:
        return "F"

# Call the function
grade = calculate_grade(85)
print(grade)   # A

# Default parameters
def greet(name, title="Student"):
    print(f"Hello, {title} {name}!")

greet("Alice")          # Hello, Student Alice!
greet("Bob", "Dr")      # Hello, Dr Bob!
```

**Why use functions?**
- Avoid writing the same code multiple times
- Each function does one thing — easier to test
- Makes code readable and organised

---

### 2.11 User Input

```python
# input() always returns a STRING
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Convert to int for calculations
age = int(input("Enter your age: "))
print(f"You were born around {2026 - age}")

# Convert to float
weight = float(input("Enter weight (kg): "))
```

**Safe input with try-except:**
```python
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        print("Marks must be between 0 and 100!")
    except ValueError:
        print("Invalid input! Please enter a number.")
```

---

---

## MODULE 3: Practice Questions

### Python Basics
1. Write a program that prints numbers 1 to 20.
2. Write a program that finds the sum of all even numbers from 1 to 100.
3. Write a function that takes a list of numbers and returns the average.
4. Write a program that counts how many vowels are in a string.
5. Create a dictionary of 5 countries and their capitals. Print each pair.

### Conditionals and Loops
6. Write a program that prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both (1 to 30).
7. Write a while loop that keeps asking for a number until the user enters 0.
8. Write a for loop that prints a multiplication table for any number.

### Functions
9. Write a function `is_prime(n)` that returns True if n is a prime number.
10. Write a function that accepts a list of marks and returns total, average, and grade.

### Lists and Dictionaries
11. Given a list of names, sort them alphabetically and print in numbered order.
12. Write a program that counts how many times each word appears in a sentence.

---

## MODULE 4: Key Takeaways

| Concept | Summary |
|---------|---------|
| AI | Machines simulating human intelligence |
| ML | Subset of AI — learns from data |
| DL | Subset of ML — deep neural networks |
| Supervised | Learns from labelled data |
| Unsupervised | Finds patterns in unlabelled data |
| Reinforcement | Learns via trial, error, and rewards |
| Variable | Named container storing a value |
| `int` / `float` | Whole / decimal numbers |
| `str` | Text in quotes |
| `bool` | True or False |
| `if/elif/else` | Make decisions based on conditions |
| `for` loop | Repeat a fixed number of times |
| `while` loop | Repeat until a condition is False |
| `list` | Ordered, mutable collection |
| `tuple` | Ordered, immutable collection |
| `dict` | Key-value pairs |
| `def` | Define a reusable function |
| `return` | Send a value back from a function |
| `input()` | Always returns a string |
| `try/except` | Handle errors gracefully |

---

## MODULE 5: Suggested Learning Path After This Module

1. **Python for Data Science** — NumPy arrays, Pandas DataFrames, Matplotlib charts
2. **Statistics for ML** — Mean, median, standard deviation, probability
3. **Machine Learning with Scikit-learn** — Train your first real ML model
4. **Deep Learning** — TensorFlow or PyTorch
5. **Real Projects** — Build a sentiment analyser, image classifier, or recommendation system

---

*These notes were created as part of the Introduction to AI & Python learning module.*
