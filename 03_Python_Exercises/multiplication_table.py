import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: multiplication_table.py
# EXERCISE: Print Multiplication Table
# ============================================================
#
# CONCEPTS PRACTISED:
#   - For loops with range()
#   - String formatting (f-strings, alignment)
#   - Functions
#   - Input validation
#   - Nested loops (for the full grid view)
#
# FEATURES:
#   - Print table for a single number (1 to N)
#   - Print a full N x N multiplication grid
#   - Validate that input is a positive integer
# ============================================================


def get_positive_integer(prompt, max_val=20):
    """
    Prompt for a positive integer between 1 and max_val.
    Repeats until valid input is received.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print(f"  [!] Please enter a positive number (minimum 1).")
            elif value > max_val:
                print(f"  [!] Please enter a number up to {max_val} (keeps output readable).")
            else:
                return value
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number (e.g. 5).")


def print_single_table(number, up_to=10):
    """
    Print the multiplication table for a single number.
    Goes from 1 x number up to up_to x number.
    """
    print()
    print(f"  Multiplication Table for {number} (1 to {up_to})")
    print("  " + "-" * 30)
    for i in range(1, up_to + 1):
        result = number * i
        # :2d pads single-digit numbers so columns align
        print(f"  {number:>3} x {i:>2} = {result:>4}")
    print("  " + "-" * 30)


def print_multiplication_grid(size):
    """
    Print a full size x size multiplication grid.
    Rows and columns both go from 1 to size.
    """
    print()
    print(f"  {size} x {size} Multiplication Grid")
    print()

    # Header row
    header = "      |"
    for col in range(1, size + 1):
        header += f" {col:>4}"
    print("  " + header)
    print("  " + "-" * (7 + size * 5))

    # Data rows
    for row in range(1, size + 1):
        line = f"  {row:>4} |"
        for col in range(1, size + 1):
            line += f" {row * col:>4}"
        print(line)


def print_all_tables(up_to=10):
    """Print tables for every number from 1 to up_to."""
    print()
    print(f"  All multiplication tables from 1 to {up_to}:")
    for n in range(1, up_to + 1):
        print()
        print(f"  --- Table of {n} ---")
        for i in range(1, 11):
            print(f"    {n} x {i:>2} = {n * i:>3}")


# ── Main program ─────────────────────────────────────────────

print("=" * 50)
print("        MULTIPLICATION TABLE GENERATOR")
print("=" * 50)
print()
print("  What would you like to do?")
print("  1 - Print table for a single number")
print("  2 - Print a full N x N grid")
print("  3 - Print all tables from 1 to 10")
print("  0 - Exit")

while True:
    print()
    choice = input("  Enter your choice (0-3): ").strip()

    if choice == "0":
        print()
        print("  Goodbye!")
        break

    elif choice == "1":
        number = get_positive_integer("  Enter the number (1-20): ", max_val=20)
        up_to  = get_positive_integer("  Print up to which multiple? (1-20): ", max_val=20)
        print_single_table(number, up_to)

    elif choice == "2":
        size = get_positive_integer("  Enter grid size (1-12): ", max_val=12)
        print_multiplication_grid(size)

    elif choice == "3":
        print_all_tables(up_to=10)

    else:
        print("  [!] Invalid choice. Enter 0, 1, 2, or 3.")
        continue

    print()
    again = input("  Do something else? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print()
        print("  Thank you for using the Multiplication Table Generator!")
        break

# ============================================================
# EXPECTED OUTPUT SAMPLE (choice 1, number=5, up_to=10):
#
#   Multiplication Table for 5 (1 to 10)
#   ------------------------------
#     5 x  1 =    5
#     5 x  2 =   10
#     5 x  3 =   15
#     ...
#     5 x 10 =   50
# ============================================================
