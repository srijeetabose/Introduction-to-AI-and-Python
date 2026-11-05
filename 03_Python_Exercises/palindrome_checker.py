import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: palindrome_checker.py
# EXERCISE: Check Whether a Word / Number is a Palindrome
# ============================================================
#
# CONCEPTS PRACTISED:
#   - String methods (lower, replace, isalpha, isdigit)
#   - String slicing ([::-1] reversal trick)
#   - Functions
#   - Input validation
#   - While loop for repeat execution
#
# WHAT IS A PALINDROME?
#   A palindrome reads the same forwards AND backwards.
#   Examples:
#     Words   : "racecar", "level", "madam", "civic"
#     Numbers : 121, 1331, 12321
#     Phrases : "A man a plan a canal Panama"
#               (ignoring spaces and case)
# ============================================================


def is_palindrome_word(word):
    """
    Check if a single word is a palindrome.
    Comparison is case-insensitive.
    Returns True or False.
    """
    cleaned = word.strip().lower()   # remove spaces, make lowercase
    return cleaned == cleaned[::-1]  # compare with its reverse


def is_palindrome_phrase(phrase):
    """
    Check if a phrase is a palindrome.
    Ignores spaces, punctuation, and letter case.
    """
    # Keep only letters and digits, then lowercase
    cleaned = ""
    for char in phrase.lower():
        if char.isalnum():           # isalnum() = True for letters and digits
            cleaned += char
    return cleaned == cleaned[::-1]


def is_palindrome_number(number):
    """
    Check if an integer is a palindrome.
    Negative numbers are never palindromes.
    """
    if number < 0:
        return False
    number_str = str(number)
    return number_str == number_str[::-1]


def show_reversal_steps(text):
    """Show how the reversal works step by step."""
    cleaned = text.strip().lower()
    print(f"    Original : '{text}'")
    print(f"    Cleaned  : '{cleaned}'")
    print(f"    Reversed : '{cleaned[::-1]}'")
    if cleaned == cleaned[::-1]:
        print(f"    Match    : YES -> PALINDROME")
    else:
        print(f"    Match    : NO  -> NOT a palindrome")


def check_and_display(user_input):
    """
    Determine input type (number/phrase/word) and run the
    appropriate palindrome check, printing a clear result.
    """
    text = user_input.strip()

    if not text:
        print("  [!] Input cannot be empty.")
        return

    print()
    print(f"  Checking: '{text}'")
    print()

    # Show step-by-step reversal
    show_reversal_steps(text)
    print()

    # Decide which checker to use
    if text.lstrip("-").isdigit():
        # It's a number
        number = int(text)
        result = is_palindrome_number(number)
        kind   = "number"
    elif " " in text:
        # It's a phrase (multiple words)
        result = is_palindrome_phrase(text)
        kind   = "phrase"
    else:
        # Single word
        result = is_palindrome_word(text)
        kind   = "word"

    if result:
        print(f"  RESULT: '{text}' IS a palindrome {kind}! ✓")
    else:
        print(f"  RESULT: '{text}' is NOT a palindrome {kind}. ✗")


# ── Built-in demonstration ────────────────────────────────────

def run_demo():
    """Test a set of known palindromes and non-palindromes."""
    print()
    print("  Built-in Examples:")
    print("  " + "-" * 48)
    test_cases = [
        ("racecar",                     True),
        ("hello",                       False),
        ("madam",                       True),
        ("python",                      False),
        ("level",                       True),
        ("121",                         True),
        ("123",                         False),
        ("A man a plan a canal Panama", True),
        ("Was it a car or a cat I saw", True),
        ("Not a palindrome",            False),
    ]

    for text, expected in test_cases:
        if " " in text:
            result = is_palindrome_phrase(text)
        elif text.isdigit():
            result = is_palindrome_number(int(text))
        else:
            result = is_palindrome_word(text)

        status = "Palindrome    " if result else "Not Palindrome"
        mark   = "OK" if result == expected else "UNEXPECTED"
        print(f"  {status} | {text:<35} [{mark}]")
    print("  " + "-" * 48)


# ── Main program ─────────────────────────────────────────────

print("=" * 50)
print("           PALINDROME CHECKER")
print("=" * 50)
print("  A palindrome reads the same forwards and")
print("  backwards. Works for words, numbers, phrases.")

run_demo()

print()
print("-" * 50)

while True:
    print()
    user_input = input("  Enter a word, number, or phrase (or 'quit' to exit): ").strip()

    if user_input.lower() in ("quit", "q", "exit"):
        print()
        print("  Exiting Palindrome Checker. Goodbye!")
        break

    if not user_input:
        print("  [!] Input cannot be empty. Please try again.")
        continue

    check_and_display(user_input)

    print()
    again = input("  Check another? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print()
        print("  Thanks for using the Palindrome Checker!")
        break

# ============================================================
# EXPECTED OUTPUT SAMPLE:
#   Checking: 'racecar'
#   Original : 'racecar'
#   Cleaned  : 'racecar'
#   Reversed : 'racecar'
#   Match    : YES -> PALINDROME
#   RESULT: 'racecar' IS a palindrome word!
# ============================================================
