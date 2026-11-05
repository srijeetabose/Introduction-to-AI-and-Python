import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: even_odd_checker.py
# EXERCISE: Check Whether a Number is Even or Odd
# ============================================================
#
# CONCEPTS PRACTISED:
#   - User input and type conversion
#   - Modulo operator (%)
#   - if-else conditional statements
#   - Input validation with try-except
#   - Loops for repeat execution
#
# LOGIC:
#   A number is EVEN if it is divisible by 2 (remainder = 0)
#   A number is ODD  if it is NOT divisible by 2 (remainder = 1)
#   We use the modulo operator: number % 2
# ============================================================


def get_integer(prompt):
    """
    Prompt the user for an integer.
    Keeps asking until a valid integer is entered.
    Returns the integer value.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number (e.g. 4, -7, 0).")


def check_even_odd(number):
    """
    Determine whether a number is even or odd.
    Returns 'Even' or 'Odd' as a string.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def classify_number(number):
    """
    Return additional classification: positive, negative, or zero.
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def display_result(number):
    """Print a formatted result for the given number."""
    parity       = check_even_odd(number)
    sign         = classify_number(number)
    divisible_5  = "Yes" if number % 5 == 0 else "No"
    divisible_10 = "Yes" if number % 10 == 0 else "No"

    print()
    print("  +-----------------------+----------+")
    print("  | Property              | Result   |")
    print("  +-----------------------+----------+")
    print(f"  | Number                | {number:<8} |")
    print(f"  | Even or Odd           | {parity:<8} |")
    print(f"  | Sign                  | {sign:<8} |")
    print(f"  | Divisible by 5?       | {divisible_5:<8} |")
    print(f"  | Divisible by 10?      | {divisible_10:<8} |")
    print("  +-----------------------+----------+")


def run_batch_check():
    """Check a predefined range and show even/odd breakdown."""
    print()
    print("  Numbers 1-20 classified:")
    evens = []
    odds  = []
    for n in range(1, 21):
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
    print(f"  Even: {evens}")
    print(f"  Odd : {odds}")


# ── Main program ─────────────────────────────────────────────
print("=" * 50)
print("         EVEN / ODD CHECKER")
print("=" * 50)

# Show a built-in batch demo first
run_batch_check()

print()
print("-" * 50)

# Interactive loop — user can check multiple numbers
while True:
    print()
    number = get_integer("  Enter a number to check (or 0 to quit): ")

    if number == 0:
        print()
        print("  Exiting Even/Odd Checker. Goodbye!")
        break

    display_result(number)

    # Ask to continue
    again = input("\n  Check another number? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print()
        print("  Thanks for using the Even/Odd Checker!")
        break

# ============================================================
# EXPECTED OUTPUT SAMPLE:
#   Numbers 1-20 classified:
#   Even: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#   Odd : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#
#   Enter a number to check (or 0 to quit): abc
#   [!] Invalid input. Please enter a whole number.
#
#   Enter a number to check (or 0 to quit): 15
#   | Number          | 15       |
#   | Even or Odd     | Odd      |
#   | Divisible by 5? | Yes      |
# ============================================================
