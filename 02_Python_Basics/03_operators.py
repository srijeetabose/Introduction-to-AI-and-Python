import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 03_operators.py
# TOPIC: Operators in Python
# ============================================================
#
# WHAT ARE OPERATORS?
# Operators are symbols that perform operations on values.
# Python has several types:
#   1. Arithmetic Operators   â†’ math calculations
#   2. Comparison Operators   â†’ compare two values
#   3. Logical Operators      â†’ combine True/False conditions
#   4. Assignment Operators   â†’ assign/update variable values
#   5. Modulo & Floor Division â†’ special but very useful
# ============================================================

print("=" * 55)
print("            OPERATORS IN PYTHON")
print("=" * 55)

# -----------------------------------------------------------
# 1. ARITHMETIC OPERATORS
# -----------------------------------------------------------
print("\n--- 1. Arithmetic Operators ---")

a = 15
b = 4

print(f"Values: a = {a}, b = {b}")
print()

# Addition
result = a + b
print(f"  Addition       : {a} + {b} = {result}")

# Subtraction
result = a - b
print(f"  Subtraction    : {a} - {b} = {result}")

# Multiplication
result = a * b
print(f"  Multiplication : {a} * {b} = {result}")

# Division (always returns float)
result = a / b
print(f"  Division       : {a} / {b} = {result}")

# Floor Division (rounds DOWN to nearest whole number)
result = a // b
print(f"  Floor Division : {a} // {b} = {result}  â† drops the decimal")

# Modulo (gives the REMAINDER after division)
result = a % b
print(f"  Modulo         : {a} % {b} = {result}  â† remainder of {a}Ã·{b}")

# Exponentiation (power)
result = a ** 2
print(f"  Exponent       : {a} ** 2 = {result}  â† {a} squared")

# -----------------------------------------------------------
# PRACTICAL ARITHMETIC EXAMPLE
# -----------------------------------------------------------
print("\n--- Practical Example: Bill Calculation ---")

item_price = 250.00
quantity = 3
discount = 50.00
tax_rate = 0.18        # 18% tax

subtotal = item_price * quantity
after_discount = subtotal - discount
tax_amount = after_discount * tax_rate
total = after_discount + tax_amount

print(f"  Item Price   : â‚¹{item_price}")
print(f"  Quantity     : {quantity}")
print(f"  Subtotal     : â‚¹{subtotal}")
print(f"  Discount     : â‚¹{discount}")
print(f"  After Disc.  : â‚¹{after_discount}")
print(f"  Tax (18%)    : â‚¹{tax_amount:.2f}")
print(f"  TOTAL        : â‚¹{total:.2f}")

# -----------------------------------------------------------
# 2. COMPARISON OPERATORS
# -----------------------------------------------------------
print("\n--- 2. Comparison Operators ---")
print("  (These always return True or False)\n")

x = 10
y = 20

print(f"  Values: x = {x}, y = {y}")
print()
print(f"  x == y  (equal to)            : {x == y}")
print(f"  x != y  (not equal to)        : {x != y}")
print(f"  x > y   (greater than)        : {x > y}")
print(f"  x < y   (less than)           : {x < y}")
print(f"  x >= y  (greater or equal)    : {x >= y}")
print(f"  x <= y  (less or equal)       : {x <= y}")

# Practical use â€” comparing marks
print("\n--- Comparing Student Marks ---")
student_marks = 72
passing_marks = 50

print(f"  Student Marks : {student_marks}")
print(f"  Passing Marks : {passing_marks}")
print(f"  Did student pass? (marks >= passing): {student_marks >= passing_marks}")

# -----------------------------------------------------------
# 3. LOGICAL OPERATORS
# -----------------------------------------------------------
print("\n--- 3. Logical Operators ---")
print("  (Combine multiple conditions)\n")

age = 20
has_id = True
is_member = False

print(f"  age = {age}, has_id = {has_id}, is_member = {is_member}")
print()

# AND â†’ True only if BOTH conditions are True
print(f"  age >= 18 AND has_id â†’ {age >= 18} AND {has_id} = {age >= 18 and has_id}")

# OR â†’ True if AT LEAST ONE condition is True
print(f"  has_id OR is_member  â†’ {has_id} OR {is_member} = {has_id or is_member}")

# NOT â†’ Flips True to False and False to True
print(f"  NOT is_member        â†’ NOT {is_member} = {not is_member}")

# Combined logical conditions
can_enter = age >= 18 and has_id
print(f"\n  Can enter (age>=18 AND has_id): {can_enter}")

gets_discount = is_member or age < 18
print(f"  Gets discount (member OR under 18): {gets_discount}")

# -----------------------------------------------------------
# 4. ASSIGNMENT OPERATORS
# -----------------------------------------------------------
print("\n--- 4. Assignment Operators ---")

score = 100             # Basic assignment
print(f"  Initial score : {score}")

score += 10             # Same as: score = score + 10
print(f"  After += 10   : {score}")

score -= 15             # Same as: score = score - 15
print(f"  After -= 15   : {score}")

score *= 2              # Same as: score = score * 2
print(f"  After *= 2    : {score}")

score //= 3             # Same as: score = score // 3
print(f"  After //= 3   : {score}")

score %= 50             # Same as: score = score % 50
print(f"  After %= 50   : {score}")

# -----------------------------------------------------------
# 5. MODULO PRACTICAL USES
# -----------------------------------------------------------
print("\n--- 5. Practical Uses of Modulo (%) ---")

# Check if a number is even or odd
number = 17
if number % 2 == 0:
    print(f"  {number} is Even")
else:
    print(f"  {number} is Odd")

# Check leap year (divisible by 4)
year = 2024
if year % 4 == 0:
    print(f"  {year} is a Leap Year")
else:
    print(f"  {year} is NOT a Leap Year")

print("\n" + "=" * 55)
print("  QUICK REFERENCE")
print("=" * 55)
print("  +   Addition       |  ==  Equal")
print("  -   Subtraction    |  !=  Not Equal")
print("  *   Multiplication |  >   Greater Than")
print("  /   Division       |  <   Less Than")
print("  //  Floor Division |  and Both must be True")
print("  %   Modulo         |  or  One must be True")
print("  **  Power/Exponent |  not Flip True/False")
print("=" * 55)

# ============================================================
# EXPECTED OUTPUT (partial):
#   Addition       : 15 + 4 = 19
#   Subtraction    : 15 - 4 = 11
#   Floor Division : 15 // 4 = 3
#   Modulo         : 15 % 4 = 3
#   x == y  : False
#   17 is Odd
#   2024 is a Leap Year
# ============================================================

