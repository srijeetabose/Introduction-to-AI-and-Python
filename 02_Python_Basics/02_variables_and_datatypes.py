import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 02_variables_and_datatypes.py
# TOPIC: Variables and Data Types
# ============================================================
#
# WHAT IS A VARIABLE?
# A variable is a named container that stores a value.
# Think of it like a labelled box â€” you put something in it
# and refer to it by the label (variable name).
#
# PYTHON DATA TYPES COVERED:
#   int   â†’ Whole numbers          (e.g., 25, -10, 0)
#   float â†’ Decimal numbers        (e.g., 3.14, -0.5)
#   str   â†’ Text / String          (e.g., "Alice", "Hello")
#   bool  â†’ True or False          (e.g., True, False)
# ============================================================

print("=" * 50)
print("       VARIABLES AND DATA TYPES IN PYTHON")
print("=" * 50)

# -----------------------------------------------------------
# 1. INTEGER (int) â€” Whole numbers, no decimal point
# -----------------------------------------------------------
print("\n--- 1. Integer (int) ---")

student_age = 20          # Age is a whole number
number_of_students = 35   # Count is a whole number
year = 2026               # Year is a whole number
negative_number = -15     # Integers can be negative

print("Student Age      :", student_age)
print("Number of Students:", number_of_students)
print("Year             :", year)
print("Negative Number  :", negative_number)
print("Data type of age :", type(student_age))   # type() tells us the data type

# -----------------------------------------------------------
# 2. FLOAT (float) â€” Numbers with a decimal point
# -----------------------------------------------------------
print("\n--- 2. Float (float) ---")

temperature = 36.6        # Body temperature
pi = 3.14159              # Mathematical constant
bank_balance = 1500.75    # Money (has cents/paise)
height = 5.9              # Height in feet

print("Temperature  :", temperature, "Â°C")
print("Pi           :", pi)
print("Bank Balance : $", bank_balance)
print("Height       :", height, "feet")
print("Data type of pi:", type(pi))

# -----------------------------------------------------------
# 3. STRING (str) â€” Text enclosed in quotes
# -----------------------------------------------------------
print("\n--- 3. String (str) ---")

student_name = "Alice Johnson"   # Double quotes
city = 'New York'                # Single quotes also work
greeting = "Hello, World!"
course_name = "Introduction to AI & Python"

print("Student Name :", student_name)
print("City         :", city)
print("Greeting     :", greeting)
print("Course       :", course_name)
print("Data type of name:", type(student_name))

# String with a number inside quotes is still a string!
zip_code = "10001"
print("Zip Code     :", zip_code, "â† This is a string, not an int!")
print("Data type    :", type(zip_code))

# -----------------------------------------------------------
# 4. BOOLEAN (bool) â€” Only True or False
# -----------------------------------------------------------
print("\n--- 4. Boolean (bool) ---")

is_student = True          # Yes/No, On/Off values
has_passed = False
is_raining = True
is_weekend = False

print("Is Student   :", is_student)
print("Has Passed   :", has_passed)
print("Is Raining   :", is_raining)
print("Is Weekend   :", is_weekend)
print("Data type    :", type(is_student))

# -----------------------------------------------------------
# 5. CHECKING DATA TYPES with type()
# -----------------------------------------------------------
print("\n--- 5. Checking Data Types ---")

a = 42
b = 3.14
c = "Python"
d = True

print(f"Value: {a}       â†’ Type: {type(a)}")
print(f"Value: {b}     â†’ Type: {type(b)}")
print(f"Value: {c}   â†’ Type: {type(c)}")
print(f"Value: {d}      â†’ Type: {type(d)}")

# -----------------------------------------------------------
# 6. TYPE CONVERSION â€” Converting between types
# -----------------------------------------------------------
print("\n--- 6. Type Conversion ---")

# Convert string to integer
age_as_string = "25"
age_as_int = int(age_as_string)
print(f"String '25' converted to int: {age_as_int} â†’ Type: {type(age_as_int)}")

# Convert integer to float
whole_number = 7
as_float = float(whole_number)
print(f"Integer 7 converted to float: {as_float} â†’ Type: {type(as_float)}")

# Convert number to string
score = 95
score_as_text = str(score)
print(f"Integer 95 converted to str: '{score_as_text}' â†’ Type: {type(score_as_text)}")

# -----------------------------------------------------------
# 7. MULTIPLE ASSIGNMENT â€” Assign many variables at once
# -----------------------------------------------------------
print("\n--- 7. Multiple Assignment ---")

x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# Assign same value to multiple variables
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# -----------------------------------------------------------
# 8. VARIABLE NAMING RULES
# -----------------------------------------------------------
print("\n--- 8. Naming Rules (examples) ---")

# VALID variable names
first_name = "Alice"     # snake_case (recommended in Python)
lastName = "Smith"       # camelCase (also works)
age2 = 30                # can contain numbers (not at start)
_private = "hidden"      # can start with underscore

print("first_name :", first_name)
print("lastName   :", lastName)
print("age2       :", age2)

# NOTE: Variable names CANNOT:
#   - Start with a number (1name is INVALID)
#   - Contain spaces (my name is INVALID)
#   - Use Python keywords (if, for, while, etc.)

print("\n" + "=" * 50)
print("       KEY TAKEAWAYS")
print("=" * 50)
print("  int   â†’ Whole numbers (age, count, year)")
print("  float â†’ Decimal numbers (price, height)")
print("  str   â†’ Text in quotes (name, city)")
print("  bool  â†’ True or False only")
print("  type() â†’ Tells you the data type")
print("=" * 50)

# ============================================================
# EXPECTED OUTPUT (partial):
#   --- 1. Integer (int) ---
#   Student Age      : 20
#   Data type of age : <class 'int'>
#   --- 2. Float (float) ---
#   Temperature  : 36.6 Â°C
#   --- 3. String (str) ---
#   Student Name : Alice Johnson
#   --- 4. Boolean (bool) ---
#   Is Student   : True
# ============================================================

