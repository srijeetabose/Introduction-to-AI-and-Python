import sys
sys.stdout.reconfigure(encoding='utf-8')

import random   # built-in module — no installation needed

# ============================================================
# FILE: number_guessing_game.py
# EXERCISE: Number Guessing Game
# ============================================================
#
# CONCEPTS PRACTISED:
#   - random module (random.randint)
#   - While loops
#   - if-elif-else conditionals
#   - Input validation (non-integer input)
#   - Functions
#   - Tracking attempts and scoring
#
# HOW TO PLAY:
#   The computer picks a secret number within a range.
#   The player guesses until they find it.
#   After each guess the game says "Too High" or "Too Low".
#   The player wins when they guess correctly.
#   Score is based on number of attempts used.
# ============================================================


# ── Constants ─────────────────────────────────────────────────
RANGE_MIN    = 1
RANGE_MAX    = 100
MAX_ATTEMPTS = 10


def get_difficulty():
    """
    Let the player choose a difficulty level.
    Returns (range_max, max_attempts) tuple.
    """
    print()
    print("  Select Difficulty:")
    print("  1 - Easy   (1 to 50,  15 attempts)")
    print("  2 - Medium (1 to 100, 10 attempts)")
    print("  3 - Hard   (1 to 200,  7 attempts)")
    print()

    while True:
        choice = input("  Your choice (1/2/3): ").strip()
        if choice == "1":
            return 50, 15, "Easy"
        elif choice == "2":
            return 100, 10, "Medium"
        elif choice == "3":
            return 200, 7, "Hard"
        else:
            print("  [!] Invalid choice. Enter 1, 2, or 3.")


def get_guess(range_min, range_max):
    """
    Prompt the player for a guess within the valid range.
    Returns a validated integer.
    """
    while True:
        try:
            guess = int(input(f"  Your guess ({range_min}-{range_max}): "))
            if guess < range_min or guess > range_max:
                print(f"  [!] Please enter a number between {range_min} and {range_max}.")
            else:
                return guess
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


def calculate_score(attempts_used, max_attempts, difficulty_label):
    """
    Calculate a score out of 100 based on attempts used.
    Fewer attempts = higher score.
    """
    efficiency = (max_attempts - attempts_used + 1) / max_attempts
    base_score = int(efficiency * 100)

    # Difficulty bonus
    bonus = {"Easy": 0, "Medium": 10, "Hard": 25}.get(difficulty_label, 0)
    return min(100, base_score + bonus)


def give_hint(guess, secret, attempts_left):
    """
    Provide a directional hint plus a proximity hint
    when the player is running low on attempts.
    """
    diff = abs(secret - guess)

    if guess < secret:
        direction = "Too LOW! Guess higher."
    else:
        direction = "Too HIGH! Guess lower."

    # Proximity hint
    if diff <= 5:
        proximity = " (Very close!)"
    elif diff <= 15:
        proximity = " (Getting warm...)"
    elif diff <= 30:
        proximity = " (Getting cooler...)"
    else:
        proximity = " (Far away.)"

    # Panic hint when few attempts remain
    urgency = ""
    if attempts_left <= 3:
        urgency = f"  *** Only {attempts_left} attempt(s) left! ***"

    print(f"  {direction}{proximity}")
    if urgency:
        print(urgency)


def play_round():
    """
    Run one complete round of the guessing game.
    Returns True if the player wants to play again.
    """
    range_max, max_attempts, difficulty = get_difficulty()
    secret_number = random.randint(RANGE_MIN, range_max)

    print()
    print(f"  Difficulty : {difficulty}")
    print(f"  Range      : {RANGE_MIN} to {range_max}")
    print(f"  Attempts   : {max_attempts} maximum")
    print(f"  I have picked a number. Can you guess it?")
    print()

    attempts_used = 0
    previous_guesses = []

    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        print(f"  Attempt {attempts_used + 1}/{max_attempts}  |  Attempts left: {attempts_left}")

        if previous_guesses:
            print(f"  Previous guesses: {previous_guesses}")

        guess = get_guess(RANGE_MIN, range_max)
        attempts_used += 1

        # Duplicate guess check
        if guess in previous_guesses:
            print(f"  [!] You already guessed {guess}! Try a different number.")
            attempts_used -= 1    # don't count duplicate as a real attempt
            continue

        previous_guesses.append(guess)

        if guess == secret_number:
            print()
            print("  " + "=" * 40)
            print(f"  Correct! The number was {secret_number}.")
            print(f"  You found it in {attempts_used} attempt(s)!")
            score = calculate_score(attempts_used, max_attempts, difficulty)
            print(f"  Your Score: {score}/100")
            if score >= 90:
                print("  Rating: EXCELLENT!")
            elif score >= 70:
                print("  Rating: GREAT!")
            elif score >= 50:
                print("  Rating: GOOD!")
            else:
                print("  Rating: KEEP PRACTISING!")
            print("  " + "=" * 40)
            break
        else:
            give_hint(guess, secret_number, max_attempts - attempts_used)
            print()
    else:
        # Loop exhausted without a correct guess
        print()
        print("  " + "=" * 40)
        print(f"  Out of attempts! The number was {secret_number}.")
        print("  Better luck next time!")
        print("  " + "=" * 40)

    print()
    play_again = input("  Play again? (yes/no): ").strip().lower()
    return play_again in ("yes", "y")


# ── Main program ─────────────────────────────────────────────

print("=" * 50)
print("          NUMBER GUESSING GAME")
print("=" * 50)
print("  The computer picks a secret number.")
print("  You guess until you find it.")
print("  Hints guide you: Too High / Too Low.")
print("  Fewer guesses = higher score!")

games_played = 0

while True:
    games_played += 1
    print()
    print(f"  --- Round {games_played} ---")
    keep_playing = play_round()
    if not keep_playing:
        print()
        print(f"  Total rounds played: {games_played}")
        print("  Thanks for playing! Goodbye.")
        break

# ============================================================
# EXPECTED OUTPUT SAMPLE:
#   Attempt 1/10  |  Attempts left: 10
#   Your guess (1-100): 50
#   Too HIGH! Guess lower. (Getting cooler...)
#
#   Attempt 2/10  |  Attempts left: 9
#   Previous guesses: [50]
#   Your guess (1-100): abc
#   [!] Invalid input. Please enter a whole number.
# ============================================================
