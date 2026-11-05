import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 06_while_loops.py
# TOPIC: While Loops in Python
# ============================================================
#
# WHAT IS A WHILE LOOP?
# A while loop keeps repeating as long as a condition is True.
# Unlike a for loop (which has a fixed count), a while loop
# runs until the condition becomes False.
#
# SYNTAX:
#   while condition:
#       # code to repeat
#       # IMPORTANT: update the condition, or it loops forever!
#
# WARNING: If the condition never becomes False, you get
# an INFINITE LOOP â€” your program will run forever!
# Always make sure the condition eventually becomes False.
# ============================================================

print("=" * 55)
print("           WHILE LOOPS IN PYTHON")
print("=" * 55)

# -----------------------------------------------------------
# 1. BASIC WHILE LOOP â€” Counting up
# -----------------------------------------------------------
print("\n--- 1. Basic While Loop â€” Counting Up ---")

counter = 1              # initialise the counter

while counter <= 5:      # condition: keep going while counter <= 5
    print(f"  Count: {counter}")
    counter += 1         # IMPORTANT: increment counter (avoid infinite loop)

print("  Loop ended! Counter is now:", counter)

# -----------------------------------------------------------
# 2. COUNTING DOWN
# -----------------------------------------------------------
print("\n--- 2. Counting Down ---")

countdown = 10

while countdown >= 0:
    if countdown == 0:
        print("  ðŸš€ LAUNCH!")
    else:
        print(f"  T-minus {countdown}...")
    countdown -= 1       # decrement by 1 each time

# -----------------------------------------------------------
# 3. SUM OF NUMBERS UNTIL USER ENTERS 0
# -----------------------------------------------------------
print("\n--- 3. Accumulating Sum (Simulated Input) ---")

# Simulating user entering: 10, 20, 30, 15, 0 (0 = stop)
inputs = [10, 20, 30, 15, 0]
index = 0
running_total = 0

print("  Adding numbers (stops when 0 is entered):")
number = inputs[index]

while number != 0:
    running_total += number
    print(f"  Added {number} â†’ Running total: {running_total}")
    index += 1
    number = inputs[index]

print(f"  Final Total: {running_total}")

# -----------------------------------------------------------
# 4. WHILE LOOP WITH BREAK
# -----------------------------------------------------------
print("\n--- 4. While Loop with break ---")

attempts = 0
correct_password = "python2026"

# Simulated password attempts
test_passwords = ["hello", "wrong123", "python2026", "another"]

print("  Attempting to log in (max 3 tries):")

while attempts < 3:
    entered = test_passwords[attempts]
    attempts += 1
    print(f"  Attempt {attempts}: Trying '{entered}'")

    if entered == correct_password:
        print("  âœ… Access Granted! Login successful.")
        break
else:
    # This only runs if the loop finished WITHOUT a break
    print("  âŒ Too many failed attempts. Account locked.")

# -----------------------------------------------------------
# 5. WHILE LOOP WITH CONTINUE
# -----------------------------------------------------------
print("\n--- 5. While Loop with continue ---")

number = 0
print("  Numbers from 1 to 10 (skipping 5 and 7):")

while number < 10:
    number += 1
    if number == 5 or number == 7:
        continue         # skip to next iteration without printing
    print(f"  {number}", end="  ")
print()

# -----------------------------------------------------------
# 6. FINDING FIRST NUMBER DIVISIBLE BY BOTH 3 AND 7
# -----------------------------------------------------------
print("\n--- 6. Finding First Number Divisible by 3 AND 7 ---")

num = 1
while True:             # This looks like infinite loop, but break saves us
    if num % 3 == 0 and num % 7 == 0:
        print(f"  First number divisible by both 3 and 7: {num}")
        break
    num += 1

# -----------------------------------------------------------
# 7. DIGIT SUM USING WHILE LOOP
# -----------------------------------------------------------
print("\n--- 7. Sum of Digits ---")

number = 9876
original = number
digit_sum = 0

print(f"  Finding digit sum of: {number}")

while number > 0:
    digit = number % 10      # get the last digit using modulo
    digit_sum += digit
    print(f"  Last digit: {digit} â†’ Running sum: {digit_sum}")
    number = number // 10    # remove the last digit

print(f"  Digit sum of {original} = {digit_sum}")

# -----------------------------------------------------------
# 8. GUESSING GAME LOGIC (no user input â€” demonstration)
# -----------------------------------------------------------
print("\n--- 8. Guessing Game Logic (Demo) ---")

secret_number = 42
guesses = [10, 60, 35, 42]   # simulated guesses
guess_index = 0
attempts = 0
max_attempts = 10

print(f"  Guess the secret number (between 1 and 100)")

while attempts < max_attempts:
    guess = guesses[guess_index]
    attempts += 1
    print(f"  Guess #{attempts}: {guess}", end=" â†’ ")

    if guess < secret_number:
        print("Too LOW! Try higher.")
    elif guess > secret_number:
        print("Too HIGH! Try lower.")
    else:
        print(f"ðŸŽ‰ CORRECT! You found it in {attempts} attempts!")
        break

    guess_index += 1
    if guess_index >= len(guesses):
        break

# -----------------------------------------------------------
# 9. WHILE VS FOR â€” WHEN TO USE WHICH
# -----------------------------------------------------------
print("\n--- 9. While vs For â€” When to Use Which ---")
print()
print("  Use FOR when:")
print("    âœ“ You know exactly how many times to repeat")
print("    âœ“ Looping over a list, string, or range")
print()
print("  Use WHILE when:")
print("    âœ“ You don't know how many times to repeat")
print("    âœ“ Waiting for a condition to change")
print("    âœ“ Building menus or interactive loops")

print("\n" + "=" * 55)
print("  KEY RULES FOR WHILE LOOPS:")
print("=" * 55)
print("  1. Always update the variable in the condition")
print("  2. Make sure the condition eventually becomes False")
print("  3. Use break to exit early when needed")
print("  4. Use continue to skip an iteration")
print("  5. 'while True:' + break is a common pattern")
print("=" * 55)

# ============================================================
# EXPECTED OUTPUT (partial):
#   Count: 1
#   Count: 2  ...  Count: 5
#   T-minus 10...  T-minus 9... ðŸš€ LAUNCH!
#   Digit sum of 9876 = 30
# ============================================================

