import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 04_conditional_statements.py
# TOPIC: Conditional Statements â€” if, elif, else
# ============================================================
#
# WHAT ARE CONDITIONAL STATEMENTS?
# They allow a program to make DECISIONS.
# Based on whether a condition is True or False,
# different blocks of code are executed.
#
# SYNTAX:
#   if condition:
#       # runs if condition is True
#   elif another_condition:
#       # runs if first was False and this is True
#   else:
#       # runs if ALL conditions above were False
#
# IMPORTANT: Python uses INDENTATION (spaces) to define
# code blocks â€” NOT curly braces like other languages.
# ============================================================

print("=" * 55)
print("     CONDITIONAL STATEMENTS IN PYTHON")
print("=" * 55)

# -----------------------------------------------------------
# 1. SIMPLE IF STATEMENT
# -----------------------------------------------------------
print("\n--- 1. Simple if Statement ---")

temperature = 38.5

# Only runs if the condition is True
if temperature > 37.5:
    print(f"  Temperature is {temperature}Â°C â€” You have a fever!")
    print("  Please consult a doctor.")

print("  (This line always runs, regardless of condition)")

# -----------------------------------------------------------
# 2. IF-ELSE STATEMENT
# -----------------------------------------------------------
print("\n--- 2. if-else Statement ---")

marks = 72
passing_marks = 50

if marks >= passing_marks:
    print(f"  Marks: {marks} â†’ You have PASSED! Congratulations!")
else:
    print(f"  Marks: {marks} â†’ You have FAILED. Please study harder.")

# -----------------------------------------------------------
# 3. IF-ELIF-ELSE STATEMENT (Multiple conditions)
# -----------------------------------------------------------
print("\n--- 3. if-elif-else Statement (Grade Calculator) ---")

percentage = 82.5

# Check conditions from top to bottom â€” first True wins
if percentage >= 90:
    grade = "A+"
    remark = "Outstanding"
elif percentage >= 80:
    grade = "A"
    remark = "Excellent"
elif percentage >= 70:
    grade = "B"
    remark = "Good"
elif percentage >= 60:
    grade = "C"
    remark = "Average"
elif percentage >= 50:
    grade = "D"
    remark = "Below Average"
else:
    grade = "F"
    remark = "Fail"

print(f"  Percentage : {percentage}%")
print(f"  Grade      : {grade}")
print(f"  Remark     : {remark}")

# -----------------------------------------------------------
# 4. NESTED IF STATEMENTS (if inside another if)
# -----------------------------------------------------------
print("\n--- 4. Nested if Statements ---")

age = 20
has_id = True

if age >= 18:
    print(f"  Age {age}: You are an adult.")
    # Inner if â€” only reached if the outer if was True
    if has_id:
        print("  You have an ID â†’ Access granted!")
    else:
        print("  No ID found â†’ Access denied.")
else:
    print(f"  Age {age}: You are a minor. Access denied.")

# -----------------------------------------------------------
# 5. MULTIPLE CONDITIONS WITH AND / OR
# -----------------------------------------------------------
print("\n--- 5. Multiple Conditions with and / or ---")

username = "admin"
password = "python123"

# Both must be correct to log in
if username == "admin" and password == "python123":
    print("  Login SUCCESSFUL! Welcome, Admin.")
else:
    print("  Login FAILED! Invalid username or password.")

# Check eligibility for a loan
age = 25
annual_income = 400000
credit_score = 720

if age >= 21 and annual_income >= 300000 and credit_score >= 650:
    print("\n  Loan Application: ELIGIBLE âœ“")
else:
    print("\n  Loan Application: NOT ELIGIBLE âœ—")

# -----------------------------------------------------------
# 6. PRACTICAL EXAMPLE â€” Traffic Light System
# -----------------------------------------------------------
print("\n--- 6. Traffic Light System ---")

light_colour = "green"

if light_colour == "red":
    print("  ðŸ”´ RED   â†’ STOP! Do not cross.")
elif light_colour == "yellow":
    print("  ðŸŸ¡ YELLOW â†’ SLOW DOWN. Prepare to stop.")
elif light_colour == "green":
    print("  ðŸŸ¢ GREEN  â†’ GO! You may proceed.")
else:
    print("  âš ï¸  Unknown signal â€” proceed with caution.")

# -----------------------------------------------------------
# 7. PRACTICAL EXAMPLE â€” Number Classification
# -----------------------------------------------------------
print("\n--- 7. Number Classification ---")

number = -7

if number > 0:
    print(f"  {number} is a POSITIVE number.")
elif number < 0:
    print(f"  {number} is a NEGATIVE number.")
else:
    print(f"  {number} is ZERO.")

# -----------------------------------------------------------
# 8. ONE-LINE IF (Ternary / Conditional Expression)
# -----------------------------------------------------------
print("\n--- 8. One-Line if (Ternary Expression) ---")

score = 65
result = "PASS" if score >= 50 else "FAIL"
print(f"  Score: {score} â†’ Result: {result}")

# Another one-liner
age = 17
status = "Adult" if age >= 18 else "Minor"
print(f"  Age: {age} â†’ Status: {status}")

print("\n" + "=" * 55)
print("  KEY RULES FOR CONDITIONALS:")
print("=" * 55)
print("  â€¢ if    â†’ Always the first condition checked")
print("  â€¢ elif  â†’ Checked only if previous was False")
print("  â€¢ else  â†’ Runs only if ALL conditions failed")
print("  â€¢ Indentation (4 spaces) defines code blocks")
print("  â€¢ == checks equality, = assigns a value")
print("=" * 55)

# ============================================================
# EXPECTED OUTPUT (partial):
#   Temperature is 38.5Â°C â€” You have a fever!
#   Marks: 72 â†’ You have PASSED! Congratulations!
#   Percentage: 82.5% â†’ Grade: A â†’ Remark: Excellent
#   Login SUCCESSFUL! Welcome, Admin.
#   ðŸŸ¢ GREEN  â†’ GO! You may proceed.
#   -7 is a NEGATIVE number.
# ============================================================

