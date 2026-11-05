# 📋 Sample Outputs

> Expected output from every program in this project.  
> Use these to verify your programs are working correctly.

---

## 02_Python_Basics

### 01_hello_world.py
```
Hello, World!
Welcome to Introduction to AI & Python!
Let's start learning Python from scratch.

--- About This Module ---
Module  : Introduction to AI & Python
Topic   : Python Programming Basics
Level   : Beginner
Language: Python 3

Both single quotes work fine too!
2026
3.14

Congratulations! You just ran your first Python program.
```

---

### 02_variables_and_datatypes.py
```
==================================================
       VARIABLES AND DATA TYPES IN PYTHON
==================================================

--- 1. Integer (int) ---
Student Age      : 20
Number of Students: 35
Year             : 2026
Negative Number  : -15
Data type of age : <class 'int'>

--- 2. Float (float) ---
Temperature  : 36.6 °C
Pi           : 3.14159
Bank Balance : $ 1500.75
Height       : 5.9 feet
Data type of pi: <class 'float'>

--- 3. String (str) ---
Student Name : Alice Johnson
City         : New York
Greeting     : Hello, World!
Course       : Introduction to AI & Python
Data type of name: <class 'str'>
Zip Code     : 10001 <- This is a string, not an int!
Data type    : <class 'str'>

--- 4. Boolean (bool) ---
Is Student   : True
Has Passed   : False
Is Raining   : True
Is Weekend   : False
Data type    : <class 'bool'>

--- 5. Checking Data Types ---
Value: 42       -> Type: <class 'int'>
Value: 3.14     -> Type: <class 'float'>
Value: Python   -> Type: <class 'str'>
Value: True     -> Type: <class 'bool'>

--- 6. Type Conversion ---
String '25' converted to int: 25 -> Type: <class 'int'>
Integer 7 converted to float: 7.0 -> Type: <class 'float'>
Integer 95 converted to str: '95' -> Type: <class 'str'>

--- 7. Multiple Assignment ---
x = 10, y = 20, z = 30
a = 100, b = 100, c = 100
```

---

### 03_operators.py
```
--- 1. Arithmetic Operators ---
Values: a = 15, b = 4

  Addition       : 15 + 4 = 19
  Subtraction    : 15 - 4 = 11
  Multiplication : 15 * 4 = 60
  Division       : 15 / 4 = 3.75
  Floor Division : 15 // 4 = 3  <- drops the decimal
  Modulo         : 15 % 4 = 3   <- remainder of 15÷4
  Exponent       : 15 ** 2 = 225  <- 15 squared

--- 2. Comparison Operators ---
  x == y  (equal to)            : False
  x != y  (not equal to)        : True
  x > y   (greater than)        : False
  x < y   (less than)           : True

--- 3. Logical Operators ---
  age >= 18 AND has_id -> True AND True = True
  has_id OR is_member  -> True OR False = True
  NOT is_member        -> NOT False = True

--- 5. Practical Uses of Modulo ---
  17 is Odd
  2024 is a Leap Year
```

---

### 04_conditional_statements.py
```
Temperature is 38.5°C — You have a fever!
Please consult a doctor.

Marks: 72 -> You have PASSED! Congratulations!

Percentage : 82.5%
Grade      : A
Remark     : Excellent

Age 20: You are an adult.
You have an ID -> Access granted!

Login SUCCESSFUL! Welcome, Admin.
Loan Application: ELIGIBLE

Traffic Light: GREEN -> GO! You may proceed.

-7 is a NEGATIVE number.

Score: 65 -> Result: PASS
Age: 17 -> Status: Minor
```

---

### 05_for_loops.py
```
--- 1. Counting with range() ---
  Counting from 0 to 4:
    0  1  2  3  4

  Even numbers from 0 to 10:
    0  2  4  6  8  10

--- 4. Sum of Numbers 1 to 100 ---
  Sum of numbers from 1 to 100 = 5050
  Sum of EVEN numbers from 1 to 100 = 2550

--- 5. Multiplication Table for 5 ---
  5 x  1 =    5
  5 x  2 =   10
  ...
  5 x 10 =   50

--- 7. break ---
  Found it! Number 6 — stopping the loop.

--- 10. Student Marks Report ---
  Name       Marks   Status
  ----------------------------
  Alice          88     PASS
  Bob            45     FAIL
  Charlie        73     PASS
  Diana          91     PASS
  Eve            62     PASS
```

---

### 06_while_loops.py
```
--- 1. Basic While Loop ---
  Count: 1
  Count: 2
  Count: 3
  Count: 4
  Count: 5
  Loop ended! Counter is now: 6

--- 2. Counting Down ---
  T-minus 10...
  T-minus 9...
  ...
  T-minus 1...
  LAUNCH!

--- 7. Sum of Digits ---
  Finding digit sum of: 9876
  Last digit: 6 -> Running sum: 6
  Last digit: 7 -> Running sum: 13
  Last digit: 8 -> Running sum: 21
  Last digit: 9 -> Running sum: 30
  Digit sum of 9876 = 30
```

---

### 07_lists_and_tuples.py
```
--- 5. List Methods ---
  Initial list: ['Apple', 'Banana', 'Cherry']
  After append('Mango')  : ['Apple', 'Banana', 'Cherry', 'Mango']
  After insert(1,...     : ['Apple', 'Blueberry', 'Banana', 'Cherry', 'Mango']
  After remove('Banana') : ['Apple', 'Blueberry', 'Cherry', 'Mango']
  After pop()            : ['Apple', 'Blueberry', 'Cherry']  | Removed: Mango
  After sort()           : ['Apple', 'Blueberry', 'Cherry']
  After reverse()        : ['Cherry', 'Blueberry', 'Apple']

--- 7. Useful List Functions ---
  Scores    : [78, 92, 55, 88, 73, 96, 45, 83]
  Minimum   : 45
  Maximum   : 96
  Total Sum : 610
  Average   : 76.25
```

---

### 08_dictionaries.py
```
--- 2. Accessing Values ---
  Name   : Alice Johnson
  Age    : 20
  Course : Computer Science
  Marks  : 88.5
  Marks (get)  : 88.5
  Phone (get)  : None
  Phone (default): N/A

--- 6. Country Capitals ---
  India                -> New Delhi
  United States        -> Washington D.C.
  United Kingdom       -> London
  Japan                -> Tokyo
  France               -> Paris

--- 8. Word Frequency Counter ---
  'dog': 1
  'fox': 2
  'jumps': 1
  'lazy': 1
  'over': 1
  'quick': 1
  'the': 3
```

---

### 09_functions.py
```
--- 7. Grade Calculator ---
  Score | Grade | Remark
  ------------------------------------
    95% |    A+ | Outstanding
    83% |     A | Excellent
    71% |     B | Good
    64% |     C | Average
    52% |     D | Below Average
    38% |     F | Fail

--- 8. Student Reports ---
  Student : Alice
  Marks   : [88, 92, 78, 95, 85]
  Total   : 438
  Average : 87.60%
  Grade   : A  (Excellent)
  Status  : PASS

  Student : Bob
  Marks   : [45, 52, 38, 60, 48]
  Total   : 243
  Average : 48.60%
  Grade   : F  (Fail)
  Status  : FAIL
```

---

### 10_user_input.py
```
--- 5. BMI Calculator (Simulated) ---
  Name   : Alice
  Weight : 65.0 kg
  Height : 1.68 m
  BMI    : 23.03
  Status : Normal weight

--- 6. Multiple Values from One Input Line ---
  Raw input  : '10 20 30'
  After split: ['10', '20', '30']
  As integers: [10, 20, 30]
  Sum        : 60
```

---

## 03_Python_Exercises

### even_odd_checker.py
```
Even: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Odd : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

Enter a number to check (or 0 to quit): abc
  [!] Invalid input. Please enter a whole number.

Enter a number to check (or 0 to quit): 15

  +-----------------------+----------+
  | Property              | Result   |
  +-----------------------+----------+
  | Number                | 15       |
  | Even or Odd           | Odd      |
  | Sign                  | Positive |
  | Divisible by 5?       | Yes      |
  | Divisible by 10?      | No       |
  +-----------------------+----------+
```

---

### calculator.py
```
Enter first number  : 0
Enter second number : abc
  [!] Invalid input. Please enter a number.
Enter second number : 0
  [!] Error: Division by zero is not allowed.

[Addition]   10.0 + 5.0 = 15
[Power]      2.0 ** 10.0 = 1024
```

---

### multiplication_table.py
```
  Multiplication Table for 7 (1 to 10)
  ------------------------------
    7 x  1 =    7
    7 x  2 =   14
    7 x  3 =   21
    7 x  4 =   28
    7 x  5 =   35
    7 x  6 =   42
    7 x  7 =   49
    7 x  8 =   56
    7 x  9 =   63
    7 x 10 =   70
  ------------------------------
```

---

### palindrome_checker.py
```
  Palindrome     | racecar                            [OK]
  Not Palindrome | hello                              [OK]
  Palindrome     | madam                              [OK]
  Palindrome     | 121                                [OK]
  Palindrome     | A man a plan a canal Panama        [OK]

  Checking: 'racecar'
  Original : 'racecar'
  Cleaned  : 'racecar'
  Reversed : 'racecar'
  Match    : YES -> PALINDROME
  RESULT: 'racecar' IS a palindrome word!
```

---

### number_guessing_game.py
```
  Difficulty : Medium
  Range      : 1 to 100
  Attempts   : 10 maximum

  Attempt 1/10  |  Attempts left: 10
  Your guess (1-100): abc
  [!] Invalid input. Please enter a whole number.
  Your guess (1-100): 150
  [!] Please enter a number between 1 and 100.
  Your guess (1-100): 50
  Too HIGH! Guess lower. (Getting cooler...)

  Attempt 2/10  |  Attempts left: 9
  Previous guesses: [50]
  Your guess (1-100): 25
  Too LOW! Guess higher. (Getting warm...)
```

---

### student_grade_calculator.py
```
  Enter student name:           <- (blank)
  [!] Name cannot be empty.

  Enter marks for Mathematics:  abc
  [!] 'abc' is not a valid number.

  Enter marks for Mathematics:  -10
  [!] Marks must be between 0 and 100.

  Enter marks for Mathematics:  88
  ...

  RESULT: ** PASS **   Grade: A (Excellent)
  Failed subjects: (none)
```

---

## 04_Mini_Project

### student_performance_analyzer.py (3 students)
```
============================================================
            STUDENT PERFORMANCE ANALYZER
============================================================

  No   Name                 Total    Avg%  Grade  Status
  --------------------------------------------------------
  1    Alice                  418   83.60%     A    PASS
  2    Bob                    345   69.00%     C    PASS
  3    Charlie                241   48.20%     F    FAIL
  --------------------------------------------------------

  Total Students : 3
  Class Average  : 66.93%
  Passed         : 2  |  Failed: 1
  Pass Rate      : 66.7%
  Highest Scorer : Alice (83.60%)
  Lowest Scorer  : Charlie (48.20%)

  Subject-wise Class Averages:
    Mathematics       65.0  [#############       ]
    Science           68.3  [#############       ]
    English           81.7  [################    ]
    History           56.0  [###########         ]
    Computer Sc.      63.7  [############        ]

  Best subject  : English  (avg 81.7)
  Weak subject  : History  (avg 56.0)
```

---

*All programs use only Python's built-in standard library. No external packages required.*
