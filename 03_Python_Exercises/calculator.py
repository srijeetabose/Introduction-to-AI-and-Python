import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: calculator.py
# EXERCISE: Basic Arithmetic Calculator
# ============================================================
#
# CONCEPTS PRACTISED:
#   - Functions (one per operation)
#   - User input and float conversion
#   - if-elif-else for operation selection
#   - Input validation (non-numeric input, division by zero)
#   - While loop for menu-driven repeat execution
#
# FEATURES:
#   - Addition, Subtraction, Multiplication, Division
#   - Floor Division and Modulo
#   - Power (exponentiation)
#   - Division-by-zero protection
#   - Handles non-numeric input gracefully
# ============================================================


# ── Operation functions ───────────────────────────────────────

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return a - b

def multiply(a, b):
    """Return a multiplied by b."""
    return a * b

def divide(a, b):
    """
    Return a divided by b.
    Raises ValueError if b is zero to prevent division by zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def floor_divide(a, b):
    """Return floor division of a by b (result rounded down)."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a // b

def modulo(a, b):
    """Return the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


# ── Input helpers ─────────────────────────────────────────────

def get_number(prompt):
    """
    Prompt for a number (int or float).
    Keeps asking until a valid number is entered.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  [!] Invalid input. Please enter a number (e.g. 5, -3.14, 0).")


def get_operation():
    """
    Display the operation menu and return the user's valid choice.
    """
    print()
    print("  Select an operation:")
    print("  +---------+----------------------+")
    print("  | Option  | Operation            |")
    print("  +---------+----------------------+")
    print("  |   1     | Addition       (+)   |")
    print("  |   2     | Subtraction    (-)   |")
    print("  |   3     | Multiplication (*)   |")
    print("  |   4     | Division       (/)   |")
    print("  |   5     | Floor Division (//)  |")
    print("  |   6     | Modulo         (%)   |")
    print("  |   7     | Power          (**)  |")
    print("  |   0     | Exit                 |")
    print("  +---------+----------------------+")
    print()

    while True:
        choice = input("  Enter option (0-7): ").strip()
        if choice in ("0", "1", "2", "3", "4", "5", "6", "7"):
            return choice
        print("  [!] Invalid option. Please enter a number between 0 and 7.")


def format_result(number):
    """
    Display as integer if whole number, else as float.
    E.g. 5.0 -> '5',  3.14 -> '3.14'
    """
    if number == int(number):
        return str(int(number))
    return str(round(number, 6))


# ── Main calculator loop ──────────────────────────────────────

print("=" * 50)
print("        BASIC ARITHMETIC CALCULATOR")
print("=" * 50)
print("  Performs addition, subtraction, multiplication,")
print("  division, floor division, modulo, and power.")
print("  Handles invalid inputs and division by zero.")

operation_map = {
    "1": (add,          "Addition",        "+"),
    "2": (subtract,     "Subtraction",     "-"),
    "3": (multiply,     "Multiplication",  "*"),
    "4": (divide,       "Division",        "/"),
    "5": (floor_divide, "Floor Division",  "//"),
    "6": (modulo,       "Modulo",          "%"),
    "7": (power,        "Power",           "**"),
}

calculation_count = 0

while True:
    choice = get_operation()

    if choice == "0":
        print()
        print(f"  Total calculations performed: {calculation_count}")
        print("  Thank you for using the Calculator!")
        break

    # Get the two numbers
    print()
    a = get_number("  Enter first number  : ")
    b = get_number("  Enter second number : ")

    func, name, symbol = operation_map[choice]

    # Perform the calculation with error handling
    try:
        result = func(a, b)
        calculation_count += 1
        print()
        print(f"  {format_result(a)} {symbol} {format_result(b)}")
        print(f"  = {format_result(result)}")
        print()
        print(f"  [{name}] Result: {format_result(result)}")
    except ValueError as e:
        print(f"\n  [!] Error: {e}")

    print()
    again = input("  Perform another calculation? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print()
        print(f"  Total calculations performed: {calculation_count}")
        print("  Thank you for using the Calculator!")
        break

# ============================================================
# EXPECTED OUTPUT SAMPLE:
#   Enter first number  : 15
#   Enter second number : 0
#   [!] Error: Division by zero is not allowed.
#
#   Enter first number  : abc
#   [!] Invalid input. Please enter a number.
#
#   10.0 + 5.0
#   = 15
#   [Addition] Result: 15
# ============================================================
