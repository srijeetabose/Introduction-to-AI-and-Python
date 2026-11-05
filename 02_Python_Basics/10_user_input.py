import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 10_user_input.py
# TOPIC: User Input and Type Conversion
# ============================================================
#
# WHAT IS USER INPUT?
# Python's input() function pauses the program and waits
# for the user to type something and press Enter.
# The value is ALWAYS returned as a STRING, even if the
# user types a number. So type conversion is essential.
#
# SYNTAX:
#   variable = input("Prompt message: ")
#
# TYPE CONVERSION FUNCTIONS:
#   int(x)   â†’ Convert to integer
#   float(x) â†’ Convert to decimal number
#   str(x)   â†’ Convert to string
#   bool(x)  â†’ Convert to True/False
# ============================================================

print("=" * 55)
print("       USER INPUT AND TYPE CONVERSION")
print("=" * 55)

# -----------------------------------------------------------
# DEMONSTRATION MODE
# -----------------------------------------------------------
# NOTE: This file demonstrates input() with simulated values
# to allow automated execution. In a real program you would
# remove the simulation lines and uncomment the input() lines.
# -----------------------------------------------------------

# -----------------------------------------------------------
# 1. BASIC STRING INPUT
# -----------------------------------------------------------
print("\n--- 1. Basic String Input ---")

# REAL CODE (uncomment when running interactively):
# name = input("Enter your name: ")

# SIMULATION (for demonstration):
name = "Alice"
print(f"  (Simulated input) â†’ '{name}'")
print(f"  Hello, {name}! Welcome to Python.")
print(f"  Data type: {type(name)}")  # input() always gives str

# -----------------------------------------------------------
# 2. NUMERIC INPUT â€” Requires Type Conversion
# -----------------------------------------------------------
print("\n--- 2. Numeric Input with int() Conversion ---")

# input() returns STRING â€” must convert to int for calculations
# age = int(input("Enter your age: "))

age_str = "20"                    # simulate: user typed "20"
age = int(age_str)                # convert string "20" to integer 20
print(f"  Raw input string : '{age_str}'  â†’ Type: {type(age_str)}")
print(f"  After int()      : {age}        â†’ Type: {type(age)}")

birth_year = 2026 - age
print(f"  Born around year : {birth_year}")

# -----------------------------------------------------------
# 3. FLOAT INPUT
# -----------------------------------------------------------
print("\n--- 3. Float Input with float() Conversion ---")

# price = float(input("Enter the price: "))

price_str = "149.99"
price = float(price_str)
print(f"  Input string : '{price_str}'  â†’ Type: {type(price_str)}")
print(f"  After float(): {price}    â†’ Type: {type(price)}")

quantity = 3
total = price * quantity
print(f"  Total for {quantity} items at â‚¹{price}: â‚¹{total:.2f}")

# -----------------------------------------------------------
# 4. INPUT VALIDATION â€” Handling Bad Input
# -----------------------------------------------------------
print("\n--- 4. Input Validation with try-except ---")

# When user types text instead of a number, int() would crash.
# try-except lets us handle that gracefully.

def safe_int_input(prompt, simulated_value):
    """Convert input to int safely, retry on invalid input."""
    try:
        value = int(simulated_value)
        print(f"  {prompt} â†’ '{simulated_value}' â†’ Accepted: {value}")
        return value
    except ValueError:
        print(f"  {prompt} â†’ '{simulated_value}' â†’ âŒ Invalid! Not a number.")
        return None

safe_int_input("Enter marks:", "85")      # valid
safe_int_input("Enter marks:", "abc")     # invalid
safe_int_input("Enter marks:", "92.5")    # invalid for int (would need float)

# -----------------------------------------------------------
# 5. COMPLETE INTERACTIVE EXAMPLE â€” BMI Calculator (Simulated)
# -----------------------------------------------------------
print("\n--- 5. BMI Calculator (Simulated Input) ---")

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI = weight / (height^2)"""
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    """Return BMI category based on value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

# Simulating:
# name   = input("Enter your name: ")
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))

sim_name   = "Alice"
sim_weight = 65.0       # kg
sim_height = 1.68       # meters

bmi = calculate_bmi(sim_weight, sim_height)
category = bmi_category(bmi)

print(f"  Name   : {sim_name}")
print(f"  Weight : {sim_weight} kg")
print(f"  Height : {sim_height} m")
print(f"  BMI    : {bmi:.2f}")
print(f"  Status : {category}")

# -----------------------------------------------------------
# 6. MULTIPLE INPUTS ON ONE LINE (using split)
# -----------------------------------------------------------
print("\n--- 6. Multiple Values from One Input Line ---")

# In real code:
# values = input("Enter 3 numbers separated by spaces: ").split()

raw_input = "10 20 30"
values = raw_input.split()          # split by whitespace
numbers = [int(v) for v in values]  # convert each to int

print(f"  Raw input  : '{raw_input}'")
print(f"  After split: {values}")
print(f"  As integers: {numbers}")
print(f"  Sum        : {sum(numbers)}")

# -----------------------------------------------------------
# 7. YES/NO INPUT
# -----------------------------------------------------------
print("\n--- 7. Yes/No Input Handling ---")

def process_yes_no(answer):
    """Process a yes/no answer."""
    answer = answer.strip().lower()    # clean up input
    if answer in ("yes", "y"):
        return True
    elif answer in ("no", "n"):
        return False
    else:
        return None   # invalid input

responses = ["Yes", "NO", "y", "n", "maybe"]
for response in responses:
    result = process_yes_no(response)
    if result is True:
        print(f"  '{response}' â†’ User said YES")
    elif result is False:
        print(f"  '{response}' â†’ User said NO")
    else:
        print(f"  '{response}' â†’ âŒ Invalid response")

# -----------------------------------------------------------
# 8. STRING FORMATTING FOR OUTPUT
# -----------------------------------------------------------
print("\n--- 8. Formatting Output ---")

student_name   = "Charlie"
student_age    = 19
student_marks  = 87.5
student_grade  = "A"

# Method 1: f-string (recommended, Python 3.6+)
print(f"  f-string : Hello {student_name}, you scored {student_marks:.1f}%")

# Method 2: .format()
print("  .format(): Hello {}, you scored {:.1f}%".format(student_name, student_marks))

# Method 3: % formatting (old style)
print("  %% style : Hello %s, age %d, marks %.1f" % (student_name, student_age, student_marks))

# Formatted table
print()
print(f"  {'Name':<12} {'Age':>4} {'Marks':>6} {'Grade':>6}")
print("  " + "-" * 32)
print(f"  {student_name:<12} {student_age:>4} {student_marks:>6.1f} {student_grade:>6}")

print("\n" + "=" * 55)
print("  KEY RULES FOR USER INPUT:")
print("=" * 55)
print("  input() ALWAYS returns a string")
print("  int(x)   â†’ '42'   becomes 42")
print("  float(x) â†’ '3.14' becomes 3.14")
print("  .strip() â†’ removes leading/trailing spaces")
print("  .lower() â†’ converts text to lowercase")
print("  Use try-except to handle invalid input")
print("=" * 55)

# ============================================================
# HOW TO MAKE THIS INTERACTIVE:
# Replace each simulated value with an input() call:
#
#   name   = input("Enter your name: ")
#   age    = int(input("Enter your age: "))
#   weight = float(input("Enter weight (kg): "))
#   height = float(input("Enter height (m): "))
# ============================================================

