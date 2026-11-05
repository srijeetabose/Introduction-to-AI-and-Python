import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 05_for_loops.py
# TOPIC: For Loops in Python
# ============================================================
#
# WHAT IS A FOR LOOP?
# A for loop lets you repeat a block of code a specific
# number of times, or go through each item in a collection.
#
# SYNTAX:
#   for variable in sequence:
#       # code to repeat
#
# The loop runs ONCE for each item in the sequence.
# ============================================================

print("=" * 55)
print("           FOR LOOPS IN PYTHON")
print("=" * 55)

# -----------------------------------------------------------
# 1. LOOP THROUGH A RANGE OF NUMBERS
# -----------------------------------------------------------
print("\n--- 1. Counting with range() ---")

# range(5) â†’ generates numbers: 0, 1, 2, 3, 4
print("  Counting from 0 to 4:")
for number in range(5):
    print(f"    {number}")

# range(1, 6) â†’ starts at 1, stops BEFORE 6: 1, 2, 3, 4, 5
print("\n  Counting from 1 to 5:")
for number in range(1, 6):
    print(f"    {number}")

# range(0, 11, 2) â†’ starts at 0, stops before 11, step 2
print("\n  Even numbers from 0 to 10:")
for number in range(0, 11, 2):
    print(f"    {number}", end="  ")   # end=" " keeps output on same line
print()   # move to next line after the loop

# -----------------------------------------------------------
# 2. LOOP THROUGH A STRING
# -----------------------------------------------------------
print("\n--- 2. Iterating Through a String ---")

word = "Python"
print(f"  Letters in '{word}':")
for letter in word:
    print(f"    {letter}")

# -----------------------------------------------------------
# 3. LOOP THROUGH A LIST
# -----------------------------------------------------------
print("\n--- 3. Looping Through a List ---")

fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print("  Fruits in the list:")
for fruit in fruits:
    print(f"    ðŸŽ {fruit}")

# Loop with index using enumerate()
print("\n  Fruits with numbering (using enumerate):")
for index, fruit in enumerate(fruits, start=1):
    print(f"    {index}. {fruit}")

# -----------------------------------------------------------
# 4. SUMMING NUMBERS WITH A LOOP
# -----------------------------------------------------------
print("\n--- 4. Sum of Numbers 1 to 100 ---")

total = 0
for number in range(1, 101):   # 1 to 100 inclusive
    total += number             # same as: total = total + number

print(f"  Sum of numbers from 1 to 100 = {total}")

# Sum only even numbers
even_sum = 0
for number in range(1, 101):
    if number % 2 == 0:        # check if number is even
        even_sum += number

print(f"  Sum of EVEN numbers from 1 to 100 = {even_sum}")

# -----------------------------------------------------------
# 5. MULTIPLICATION TABLE
# -----------------------------------------------------------
print("\n--- 5. Multiplication Table for 5 ---")

table_number = 5
for i in range(1, 11):
    result = table_number * i
    print(f"  {table_number} x {i:2d} = {result}")

# -----------------------------------------------------------
# 6. NESTED FOR LOOPS (loop inside a loop)
# -----------------------------------------------------------
print("\n--- 6. Nested Loop â€” Simple Star Pattern ---")

rows = 5
for i in range(1, rows + 1):
    for j in range(i):          # inner loop runs i times
        print("*", end="")      # print star without newline
    print()                     # move to next line after each row

# -----------------------------------------------------------
# 7. BREAK â€” Exit the loop early
# -----------------------------------------------------------
print("\n--- 7. break â€” Stop Loop Early ---")

print("  Searching for the number 6:")
for number in range(1, 11):
    if number == 6:
        print(f"  Found it! Number {number} â€” stopping the loop.")
        break                   # immediately exits the loop
    print(f"  Checking: {number}")

# -----------------------------------------------------------
# 8. CONTINUE â€” Skip current iteration
# -----------------------------------------------------------
print("\n--- 8. continue â€” Skip an Iteration ---")

print("  Printing 1 to 10, skipping multiples of 3:")
for number in range(1, 11):
    if number % 3 == 0:
        continue                # skip this iteration, go to next
    print(f"    {number}", end="  ")
print()

# -----------------------------------------------------------
# 9. FOR-ELSE (rarely used but good to know)
# -----------------------------------------------------------
print("\n--- 9. for-else Block ---")

# The 'else' runs ONLY if the loop completed WITHOUT a break
target = 15
for number in range(1, 11):
    if number == target:
        print(f"  Found {target} in range!")
        break
else:
    # This runs because the loop finished without hitting break
    print(f"  {target} was NOT found in range(1, 11).")

# -----------------------------------------------------------
# 10. PRACTICAL EXAMPLE â€” Student Marks Processing
# -----------------------------------------------------------
print("\n--- 10. Student Marks Report ---")

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
marks    = [88, 45, 73, 91, 62]

print(f"  {'Name':<10} {'Marks':>6} {'Status':>8}")
print("  " + "-" * 28)

for i in range(len(students)):
    name = students[i]
    mark = marks[i]
    status = "PASS" if mark >= 50 else "FAIL"
    print(f"  {name:<10} {mark:>6} {status:>8}")

print("\n" + "=" * 55)
print("  KEY CONCEPTS:")
print("=" * 55)
print("  range(n)         â†’ 0 to n-1")
print("  range(a, b)      â†’ a to b-1")
print("  range(a, b, step)â†’ a to b-1 with step size")
print("  enumerate()      â†’ gives index + value")
print("  break            â†’ exit loop immediately")
print("  continue         â†’ skip to next iteration")
print("=" * 55)

# ============================================================
# EXPECTED OUTPUT (partial):
#   Counting from 1 to 5: 1 2 3 4 5
#   Sum of numbers from 1 to 100 = 5050
#   5 x  1 = 5
#   5 x  2 = 10  ...
# ============================================================

