import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 09_functions.py
# TOPIC: Functions in Python
# ============================================================
#
# WHAT IS A FUNCTION?
# A function is a named, reusable block of code that performs
# a specific task. Instead of writing the same code multiple
# times, you define it once and CALL it whenever needed.
#
# WHY USE FUNCTIONS?
#   - Avoid repetition (write once, use many times)
#   - Make code organised and readable
#   - Easier to test and debug individual pieces
#   - Break a large problem into smaller sub-problems
#
# SYNTAX:
#   def function_name(parameter1, parameter2):
#       """Docstring: describes what the function does."""
#       # code goes here
#       return result    # (optional)
# ============================================================

print("=" * 55)
print("           FUNCTIONS IN PYTHON")
print("=" * 55)

# -----------------------------------------------------------
# 1. DEFINING AND CALLING A BASIC FUNCTION
# -----------------------------------------------------------
print("\n--- 1. Basic Function (No Parameters) ---")

def greet():
    """Prints a welcome greeting."""
    print("  Hello! Welcome to Python Functions.")
    print("  Functions help you organise your code.")

# CALLING the function (run the code inside it)
greet()
greet()    # Can call it as many times as needed

# -----------------------------------------------------------
# 2. FUNCTION WITH PARAMETERS (inputs)
# -----------------------------------------------------------
print("\n--- 2. Function with Parameters ---")

def greet_person(name):
    """Greet a specific person by name."""
    print(f"  Hello, {name}! Nice to meet you.")

# Calling with different arguments
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

# -----------------------------------------------------------
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# -----------------------------------------------------------
print("\n--- 3. Multiple Parameters ---")

def add_numbers(a, b):
    """Add two numbers and print the result."""
    result = a + b
    print(f"  {a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(100, 250)
add_numbers(3.14, 2.86)

# -----------------------------------------------------------
# 4. FUNCTION WITH RETURN VALUE
# -----------------------------------------------------------
print("\n--- 4. Functions that Return Values ---")

def square(number):
    """Return the square of a number."""
    return number ** 2

def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width

# Store returned value in a variable
result = square(7)
print(f"  Square of 7  : {result}")
print(f"  Square of 12 : {square(12)}")

area = calculate_area(8, 5)
print(f"  Area of 8x5 rectangle: {area}")

# -----------------------------------------------------------
# 5. DEFAULT PARAMETERS (optional arguments)
# -----------------------------------------------------------
print("\n--- 5. Default Parameter Values ---")

def greet_with_title(name, title="Mr/Ms"):
    """Greet with a default title if none is provided."""
    print(f"  Good day, {title} {name}!")

greet_with_title("Alice", "Dr")       # Custom title
greet_with_title("Bob", "Prof")       # Custom title
greet_with_title("Charlie")           # Uses default "Mr/Ms"

# -----------------------------------------------------------
# 6. RETURNING MULTIPLE VALUES
# -----------------------------------------------------------
print("\n--- 6. Returning Multiple Values ---")

def get_min_max(numbers):
    """Return both the minimum and maximum of a list."""
    return min(numbers), max(numbers)

scores = [78, 92, 55, 88, 73, 96, 45]
minimum, maximum = get_min_max(scores)
print(f"  Scores   : {scores}")
print(f"  Minimum  : {minimum}")
print(f"  Maximum  : {maximum}")

# -----------------------------------------------------------
# 7. PRACTICAL FUNCTION â€” Grade Calculator
# -----------------------------------------------------------
print("\n--- 7. Grade Calculator Function ---")

def calculate_grade(percentage):
    """
    Determine letter grade based on percentage.
    Returns grade (str) and remark (str).
    """
    if percentage >= 90:
        return "A+", "Outstanding"
    elif percentage >= 80:
        return "A", "Excellent"
    elif percentage >= 70:
        return "B", "Good"
    elif percentage >= 60:
        return "C", "Average"
    elif percentage >= 50:
        return "D", "Below Average"
    else:
        return "F", "Fail"

# Test with different percentages
test_scores = [95, 83, 71, 64, 52, 38]
print(f"  {'Score':>6} | {'Grade':>5} | Remark")
print("  " + "-" * 35)
for score in test_scores:
    grade, remark = calculate_grade(score)
    print(f"  {score:>5}% | {grade:>5} | {remark}")

# -----------------------------------------------------------
# 8. FUNCTION CALLING ANOTHER FUNCTION
# -----------------------------------------------------------
print("\n--- 8. Functions Calling Other Functions ---")

def calculate_average(marks_list):
    """Calculate and return the average of a list."""
    if len(marks_list) == 0:
        return 0
    return sum(marks_list) / len(marks_list)

def student_report(name, marks_list):
    """
    Generate a full student report.
    Calls calculate_average() and calculate_grade() internally.
    """
    total = sum(marks_list)
    average = calculate_average(marks_list)
    grade, remark = calculate_grade(average)
    status = "PASS" if average >= 50 else "FAIL"

    print(f"\n  Student : {name}")
    print(f"  Marks   : {marks_list}")
    print(f"  Total   : {total}")
    print(f"  Average : {average:.2f}%")
    print(f"  Grade   : {grade}  ({remark})")
    print(f"  Status  : {status}")

student_report("Alice", [88, 92, 78, 95, 85])
student_report("Bob",   [45, 52, 38, 60, 48])

# -----------------------------------------------------------
# 9. LAMBDA (Anonymous) FUNCTIONS â€” one-line functions
# -----------------------------------------------------------
print("\n--- 9. Lambda Functions ---")

# Lambda is a quick one-line function â€” useful for simple tasks
double = lambda x: x * 2
cube   = lambda x: x ** 3
add    = lambda x, y: x + y

print(f"  double(5) = {double(5)}")
print(f"  cube(4)   = {cube(4)}")
print(f"  add(3,7)  = {add(3, 7)}")

# Lambda with sorted() â€” sort by second element of a tuple
students_marks = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("Diana", 65)]
sorted_by_marks = sorted(students_marks, key=lambda x: x[1], reverse=True)
print("\n  Students ranked by marks:")
for rank, (name, mark) in enumerate(sorted_by_marks, 1):
    print(f"    {rank}. {name}: {mark}")

# -----------------------------------------------------------
# 10. SCOPE â€” Local vs Global Variables
# -----------------------------------------------------------
print("\n--- 10. Variable Scope ---")

global_var = "I am GLOBAL"    # Available everywhere

def scope_demo():
    local_var = "I am LOCAL"  # Only available inside this function
    print(f"  Inside function: {local_var}")
    print(f"  Inside function: {global_var}")  # Can read global

scope_demo()
print(f"  Outside function: {global_var}")
# print(local_var)  â† This would raise NameError â€” local_var doesn't exist here

print("\n" + "=" * 55)
print("  FUNCTION QUICK REFERENCE:")
print("=" * 55)
print("  def name():          â†’ Define with no params")
print("  def name(a, b):      â†’ Define with params")
print("  def name(a, b=10):   â†’ Default param value")
print("  return value         â†’ Send value back to caller")
print("  result = name(args)  â†’ Call and capture result")
print("  lambda x: x*2        â†’ Quick one-line function")
print("=" * 55)

