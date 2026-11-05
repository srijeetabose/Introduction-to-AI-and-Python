import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: student_performance_analyzer.py
# PROJECT: Student Performance Analyzer
# ============================================================
#
# DISCLAIMER:
#   This is a Python-based data analysis application.
#   It does NOT use Machine Learning, AI models, or any
#   external libraries. It is purely a Python programming
#   exercise demonstrating core Python concepts.
#
# FEATURES:
#   1. Add multiple students with marks in 5 subjects
#   2. Calculate total marks and average percentage
#   3. Assign letter grades (A+, A, B, C, D, F)
#   4. Determine pass/fail status
#   5. Display full performance report
#   6. View individual student details
#   7. Show class statistics (highest, lowest, class average)
#   8. Edit or remove a student record
#   9. Handles all invalid inputs gracefully
#
# CONCEPTS USED:
#   - Functions, Lists, Dictionaries
#   - Loops (for, while), Conditionals (if/elif/else)
#   - Input validation (try-except, range checks)
#   - String formatting (f-strings, alignment)
# ============================================================

# ── Configuration ─────────────────────────────────────────────
SUBJECTS      = ["Mathematics", "Science", "English", "History", "Computer Sc."]
NUM_SUBJECTS  = len(SUBJECTS)
MAX_MARKS     = 100
PASSING_MARKS = 50    # minimum per subject to pass that subject

# Grading thresholds (percentage)
GRADE_SCALE = [
    (90, "A+", "Outstanding"),
    (80, "A",  "Excellent"),
    (70, "B",  "Good"),
    (60, "C",  "Average"),
    (50, "D",  "Below Average"),
    ( 0, "F",  "Fail"),
]


# ════════════════════════════════════════════════════════════
# SECTION 1: INPUT VALIDATION HELPERS
# ════════════════════════════════════════════════════════════

def get_valid_name(prompt, existing_names=None):
    """
    Prompt for a non-empty student name.
    - Strips whitespace
    - Rejects blank input
    - Rejects names longer than 40 characters
    - Warns (but allows) if name already exists
    Returns the validated name string.
    """
    while True:
        name = input(prompt).strip()
        if not name:
            print("  [!] Name cannot be empty. Please enter a valid name.")
            continue
        if len(name) > 40:
            print("  [!] Name too long (max 40 characters). Please shorten it.")
            continue
        if existing_names and name.lower() in [n.lower() for n in existing_names]:
            confirm = input(f"  [?] '{name}' already exists. Add anyway? (yes/no): ").strip().lower()
            if confirm not in ("yes", "y"):
                continue
        return name


def get_valid_marks(subject):
    """
    Prompt for marks in a subject.
    - Must be a number (int or float)
    - Must be between 0 and MAX_MARKS inclusive
    Returns the validated float.
    """
    while True:
        raw = input(f"    {subject:<14}: ").strip()
        if not raw:
            print(f"  [!] Marks cannot be empty. Enter a number between 0 and {MAX_MARKS}.")
            continue
        try:
            value = float(raw)
        except ValueError:
            print(f"  [!] '{raw}' is not a valid number. Enter digits only (e.g. 75 or 82.5).")
            continue
        if value < 0 or value > MAX_MARKS:
            print(f"  [!] Marks must be between 0 and {MAX_MARKS}. You entered {value}.")
            continue
        return value


def get_positive_integer(prompt, min_val=1, max_val=50):
    """Prompt for an integer within [min_val, max_val]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value < min_val or value > max_val:
                print(f"  [!] Enter a number between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print(f"  [!] '{raw}' is not a valid integer.")


# ════════════════════════════════════════════════════════════
# SECTION 2: CALCULATION FUNCTIONS
# ════════════════════════════════════════════════════════════

def calculate_grade(percentage):
    """
    Return (grade, remark) tuple based on percentage.
    Uses the GRADE_SCALE configuration list.
    """
    for threshold, grade, remark in GRADE_SCALE:
        if percentage >= threshold:
            return grade, remark
    return "F", "Fail"


def analyse_student(name, marks_list):
    """
    Compute all performance metrics for one student.

    Args:
        name       (str)  : Student name
        marks_list (list) : List of floats, one per subject

    Returns:
        dict: Contains all computed fields for this student.
    """
    total         = sum(marks_list)
    max_possible  = MAX_MARKS * NUM_SUBJECTS
    average       = total / NUM_SUBJECTS
    percentage    = (total / max_possible) * 100
    grade, remark = calculate_grade(percentage)

    # Pass only if EVERY subject is >= PASSING_MARKS
    subject_results = []
    all_passed = True
    for i, mark in enumerate(marks_list):
        passed = mark >= PASSING_MARKS
        if not passed:
            all_passed = False
        subject_results.append({
            "subject": SUBJECTS[i],
            "marks"  : mark,
            "passed" : passed,
        })

    status       = "PASS" if all_passed else "FAIL"
    failed_subs  = [r["subject"] for r in subject_results if not r["passed"]]
    highest_sub  = SUBJECTS[marks_list.index(max(marks_list))]
    lowest_sub   = SUBJECTS[marks_list.index(min(marks_list))]

    return {
        "name"           : name,
        "marks"          : marks_list,
        "subject_results": subject_results,
        "total"          : total,
        "average"        : average,
        "percentage"     : percentage,
        "grade"          : grade,
        "remark"         : remark,
        "status"         : status,
        "failed_subs"    : failed_subs,
        "highest_subject": highest_sub,
        "lowest_subject" : lowest_sub,
    }


def compute_class_stats(students):
    """
    Compute class-level statistics from a list of student dicts.
    Returns a dict of class-level metrics.
    """
    if not students:
        return None

    percentages  = [s["percentage"] for s in students]
    class_avg    = sum(percentages) / len(percentages)
    top_student  = max(students, key=lambda s: s["percentage"])
    low_student  = min(students, key=lambda s: s["percentage"])
    pass_count   = sum(1 for s in students if s["status"] == "PASS")
    fail_count   = len(students) - pass_count

    # Subject-wise class averages
    sub_avgs = []
    for i in range(NUM_SUBJECTS):
        avg = sum(s["marks"][i] for s in students) / len(students)
        sub_avgs.append((SUBJECTS[i], avg))

    best_subject  = max(sub_avgs, key=lambda x: x[1])
    worst_subject = min(sub_avgs, key=lambda x: x[1])

    return {
        "total_students" : len(students),
        "class_avg"      : class_avg,
        "top_student"    : top_student,
        "low_student"    : low_student,
        "pass_count"     : pass_count,
        "fail_count"     : fail_count,
        "pass_rate"      : (pass_count / len(students)) * 100,
        "sub_avgs"       : sub_avgs,
        "best_subject"   : best_subject,
        "worst_subject"  : worst_subject,
    }


# ════════════════════════════════════════════════════════════
# SECTION 3: DISPLAY FUNCTIONS
# ════════════════════════════════════════════════════════════

def print_header(title):
    """Print a centred section header."""
    width = 60
    print()
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def display_individual_card(student):
    """Print a detailed result card for one student."""
    print()
    print("  " + "=" * 56)
    print("             INDIVIDUAL STUDENT REPORT")
    print("  " + "=" * 56)
    print(f"  Student   : {student['name']}")
    print(f"  Grade     : {student['grade']}  ({student['remark']})")
    print(f"  Status    : {student['status']}")
    print("  " + "-" * 56)
    print(f"  {'Subject':<16} {'Marks':>6}/{MAX_MARKS}  {'Subject Status':>14}")
    print("  " + "-" * 56)

    for res in student["subject_results"]:
        sub_status = "Pass" if res["passed"] else "FAIL"
        bar_filled = int(res["marks"] / MAX_MARKS * 20)
        bar        = "#" * bar_filled + "-" * (20 - bar_filled)
        print(f"  {res['subject']:<16} {res['marks']:>6.1f}       {sub_status:>14}  [{bar}]")

    print("  " + "-" * 56)
    print(f"  {'Total':<16} {student['total']:>6.1f}/{MAX_MARKS * NUM_SUBJECTS}")
    print(f"  {'Average':<16} {student['average']:>6.1f}")
    print(f"  {'Percentage':<16} {student['percentage']:>6.2f}%")
    print("  " + "-" * 56)

    if student["status"] == "FAIL" and student["failed_subs"]:
        print(f"  Failed subjects: {', '.join(student['failed_subs'])}")

    print(f"  Best subject : {student['highest_subject']}")
    print(f"  Weak subject : {student['lowest_subject']}")
    print("  " + "=" * 56)


def display_full_report(students):
    """Print the complete class performance report table."""
    if not students:
        print("\n  [!] No students to display.")
        return

    stats = compute_class_stats(students)

    print_header("STUDENT PERFORMANCE REPORT")
    print()
    print(f"  {'No':<4} {'Name':<20} {'Total':>6} {'Avg%':>7} {'Grade':>5} {'Status':>6}")
    print("  " + "-" * 56)

    # Sort by percentage descending for ranking
    ranked = sorted(students, key=lambda s: s["percentage"], reverse=True)
    for rank, s in enumerate(ranked, 1):
        print(f"  {rank:<4} {s['name']:<20} {s['total']:>5.0f}  "
              f"{s['percentage']:>6.2f}% {s['grade']:>5} {s['status']:>6}")

    print("  " + "-" * 56)
    print()
    print(f"  Total Students : {stats['total_students']}")
    print(f"  Class Average  : {stats['class_avg']:.2f}%")
    print(f"  Passed         : {stats['pass_count']}  |  Failed: {stats['fail_count']}")
    print(f"  Pass Rate      : {stats['pass_rate']:.1f}%")
    print()
    print(f"  Highest Scorer : {stats['top_student']['name']} "
          f"({stats['top_student']['percentage']:.2f}%)")
    print(f"  Lowest Scorer  : {stats['low_student']['name']} "
          f"({stats['low_student']['percentage']:.2f}%)")
    print()
    print("  Subject-wise Class Averages:")
    for subject, avg in stats["sub_avgs"]:
        bar = "#" * int(avg / MAX_MARKS * 20)
        print(f"    {subject:<16} {avg:>5.1f}  [{bar:<20}]")
    print()
    print(f"  Best subject  : {stats['best_subject'][0]}  "
          f"(avg {stats['best_subject'][1]:.1f})")
    print(f"  Weak subject  : {stats['worst_subject'][0]}  "
          f"(avg {stats['worst_subject'][1]:.1f})")
    print("=" * 60)


def display_student_list(students):
    """Print a numbered list of current students."""
    if not students:
        print("\n  [!] No students added yet.")
        return
    print()
    print(f"  {'#':<4} {'Name':<25} {'Percentage':>10} {'Status':>6}")
    print("  " + "-" * 48)
    for i, s in enumerate(students, 1):
        print(f"  {i:<4} {s['name']:<25} {s['percentage']:>9.2f}% {s['status']:>6}")
    print("  " + "-" * 48)
    print(f"  Total: {len(students)} student(s)")


# ════════════════════════════════════════════════════════════
# SECTION 4: MENU-DRIVEN ACTIONS
# ════════════════════════════════════════════════════════════

def action_add_students(students):
    """Add one or more students interactively."""
    print()
    num = get_positive_integer(
        "  How many students do you want to add? (1-50): ",
        min_val=1, max_val=50
    )

    existing_names = [s["name"] for s in students]

    for i in range(1, num + 1):
        print()
        print(f"  --- Student {len(students) + 1} ---")
        name = get_valid_name("  Student name: ", existing_names)
        print(f"  Enter marks for {name} (0-{MAX_MARKS} per subject):")

        marks_list = []
        for subject in SUBJECTS:
            m = get_valid_marks(subject)
            marks_list.append(m)

        student_data = analyse_student(name, marks_list)
        students.append(student_data)
        existing_names.append(name)

        print()
        print(f"  Student '{name}' added successfully.")
        print(f"  Percentage: {student_data['percentage']:.2f}%  |  "
              f"Grade: {student_data['grade']}  |  Status: {student_data['status']}")

    return students


def action_view_individual(students):
    """Show the detailed card for a specific student."""
    if not students:
        print("\n  [!] No students added yet.")
        return

    display_student_list(students)
    print()
    idx = get_positive_integer(
        f"  Enter student number (1-{len(students)}): ",
        min_val=1, max_val=len(students)
    )
    display_individual_card(students[idx - 1])


def action_edit_student(students):
    """Re-enter marks for an existing student."""
    if not students:
        print("\n  [!] No students to edit.")
        return

    display_student_list(students)
    print()
    idx = get_positive_integer(
        f"  Enter student number to edit (1-{len(students)}): ",
        min_val=1, max_val=len(students)
    )
    student = students[idx - 1]
    print(f"\n  Editing marks for: {student['name']}")
    print(f"  Enter new marks (0-{MAX_MARKS} per subject):")

    marks_list = []
    for subject in SUBJECTS:
        m = get_valid_marks(subject)
        marks_list.append(m)

    students[idx - 1] = analyse_student(student["name"], marks_list)
    print(f"\n  '{student['name']}' updated successfully.")


def action_remove_student(students):
    """Remove a student from the list."""
    if not students:
        print("\n  [!] No students to remove.")
        return

    display_student_list(students)
    print()
    idx = get_positive_integer(
        f"  Enter student number to remove (1-{len(students)}): ",
        min_val=1, max_val=len(students)
    )
    name = students[idx - 1]["name"]
    confirm = input(f"  Are you sure you want to remove '{name}'? (yes/no): ").strip().lower()
    if confirm in ("yes", "y"):
        students.pop(idx - 1)
        print(f"  '{name}' removed successfully.")
    else:
        print("  Removal cancelled.")


def action_search_student(students):
    """Search for a student by name (partial match supported)."""
    if not students:
        print("\n  [!] No students added yet.")
        return

    print()
    query = input("  Enter name to search: ").strip().lower()
    matches = [s for s in students if query in s["name"].lower()]

    if not matches:
        print(f"  No students found matching '{query}'.")
    else:
        print(f"\n  Found {len(matches)} match(es):")
        for s in matches:
            display_individual_card(s)


def display_menu():
    """Print the main menu."""
    print()
    print("  +-------+------------------------------------------+")
    print("  | MENU  |  STUDENT PERFORMANCE ANALYZER            |")
    print("  +-------+------------------------------------------+")
    print("  |  1    |  Add student(s)                          |")
    print("  |  2    |  View full class report                  |")
    print("  |  3    |  View individual student report          |")
    print("  |  4    |  Edit student marks                      |")
    print("  |  5    |  Remove a student                        |")
    print("  |  6    |  Search student by name                  |")
    print("  |  7    |  List all students                       |")
    print("  |  0    |  Exit                                    |")
    print("  +-------+------------------------------------------+")
    print()


# ════════════════════════════════════════════════════════════
# SECTION 5: MAIN PROGRAM ENTRY POINT
# ════════════════════════════════════════════════════════════

def main():
    """Main program loop — menu-driven interface."""
    students = []   # master list of student dictionaries

    print_header("STUDENT PERFORMANCE ANALYZER")
    print()
    print("  Subjects  :", ", ".join(SUBJECTS))
    print(f"  Max Marks : {MAX_MARKS} per subject  "
          f"({MAX_MARKS * NUM_SUBJECTS} total)")
    print(f"  Pass Mark : {PASSING_MARKS} per subject")
    print()
    print("  GRADING SCALE:")
    for threshold, grade, remark in GRADE_SCALE:
        print(f"    {grade:<3}  {remark:<15}  (>= {threshold}%)")

    while True:
        display_menu()

        choice = input("  Enter your choice (0-7): ").strip()

        if choice == "0":
            print()
            print("  Exiting Student Performance Analyzer.")
            print(f"  Session summary: {len(students)} student(s) on record.")
            print("  Goodbye!")
            break

        elif choice == "1":
            action_add_students(students)

        elif choice == "2":
            display_full_report(students)

        elif choice == "3":
            action_view_individual(students)

        elif choice == "4":
            action_edit_student(students)

        elif choice == "5":
            action_remove_student(students)

        elif choice == "6":
            action_search_student(students)

        elif choice == "7":
            display_student_list(students)

        else:
            print("\n  [!] Invalid choice. Enter a number from 0 to 7.")


# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    main()
