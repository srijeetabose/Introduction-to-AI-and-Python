import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: student_grade_calculator.py
# EXERCISE: Student Grade Calculator
# ============================================================
#
# CONCEPTS PRACTISED:
#   - Functions
#   - Lists and dictionaries
#   - Input validation (marks range, non-numeric)
#   - for loops and range()
#   - String formatting and f-strings
#   - Arithmetic (total, average, percentage)
#
# FEATURES:
#   - Accept marks for up to 5 subjects
#   - Calculate total, average, and percentage
#   - Assign a letter grade
#   - Determine pass/fail status
#   - Display a formatted result card
#
# GRADING SCALE:
#   90 - 100  ->  A+  (Outstanding)
#   80 -  89  ->  A   (Excellent)
#   70 -  79  ->  B   (Good)
#   60 -  69  ->  C   (Average)
#   50 -  59  ->  D   (Below Average)
#   Below 50  ->  F   (Fail)
# ============================================================

SUBJECTS      = ["Mathematics", "Science", "English", "History", "Computer Science"]
MAX_MARKS     = 100
PASSING_MARKS = 50


# ── Helper functions ──────────────────────────────────────────

def get_marks(subject):
    """
    Prompt for marks in a subject.
    Validates that input is a number between 0 and MAX_MARKS.
    Returns the validated float value.
    """
    while True:
        try:
            marks = float(input(f"  Enter marks for {subject} (0-{MAX_MARKS}): "))
            if marks < 0 or marks > MAX_MARKS:
                print(f"  [!] Marks must be between 0 and {MAX_MARKS}. Try again.")
            else:
                return marks
        except ValueError:
            print(f"  [!] Invalid input. Enter a number (e.g. 75 or 82.5).")


def get_student_name():
    """Prompt for student name. Name cannot be blank."""
    while True:
        name = input("  Enter student name: ").strip()
        if not name:
            print("  [!] Name cannot be empty. Please enter a valid name.")
        elif len(name) > 50:
            print("  [!] Name too long (max 50 characters).")
        else:
            return name


def calculate_grade(percentage):
    """
    Return (grade, remark) based on percentage.
    """
    if percentage >= 90:
        return "A+", "Outstanding"
    elif percentage >= 80:
        return "A",  "Excellent"
    elif percentage >= 70:
        return "B",  "Good"
    elif percentage >= 60:
        return "C",  "Average"
    elif percentage >= 50:
        return "D",  "Below Average"
    else:
        return "F",  "Fail"


def analyse_student(name, marks_list):
    """
    Compute all statistics for one student.
    Returns a dictionary with all results.
    """
    total       = sum(marks_list)
    average     = total / len(marks_list)
    percentage  = (total / (MAX_MARKS * len(marks_list))) * 100
    grade, remark = calculate_grade(percentage)
    passed      = all(m >= PASSING_MARKS for m in marks_list)   # must pass ALL subjects
    status      = "PASS" if passed else "FAIL"
    failed_subs = [SUBJECTS[i] for i, m in enumerate(marks_list) if m < PASSING_MARKS]

    return {
        "name"        : name,
        "marks"       : marks_list,
        "total"       : total,
        "average"     : average,
        "percentage"  : percentage,
        "grade"       : grade,
        "remark"      : remark,
        "status"      : status,
        "failed_subs" : failed_subs,
    }


def display_result_card(data):
    """Print a formatted result card for one student."""
    print()
    print("  " + "=" * 52)
    print(f"             STUDENT RESULT CARD")
    print("  " + "=" * 52)
    print(f"  Student Name : {data['name']}")
    print("  " + "-" * 52)
    print(f"  {'Subject':<22} {'Marks':>6}/{MAX_MARKS}  {'Status':>8}")
    print("  " + "-" * 52)

    for i, subject in enumerate(SUBJECTS):
        m      = data['marks'][i]
        s_stat = "Pass" if m >= PASSING_MARKS else "FAIL"
        print(f"  {subject:<22} {m:>6.1f}     {s_stat:>8}")

    print("  " + "-" * 52)
    max_possible = MAX_MARKS * len(SUBJECTS)
    print(f"  {'Total Marks':<22} {data['total']:>6.1f}/{max_possible}")
    print(f"  {'Average':<22} {data['average']:>6.1f}")
    print(f"  {'Percentage':<22} {data['percentage']:>6.1f}%")
    print(f"  {'Grade':<22} {data['grade']:>6}")
    print(f"  {'Remark':<22} {data['remark']:>15}")
    print("  " + "-" * 52)

    if data['status'] == "PASS":
        print(f"  RESULT: ** PASS **   Grade: {data['grade']} ({data['remark']})")
    else:
        print(f"  RESULT: ** FAIL **")
        if data['failed_subs']:
            print(f"  Failed subjects: {', '.join(data['failed_subs'])}")

    print("  " + "=" * 52)


def collect_student_data():
    """
    Interactively collect one student's name and marks.
    Returns the analysed data dictionary.
    """
    name       = get_student_name()
    marks_list = []
    print()
    for subject in SUBJECTS:
        m = get_marks(subject)
        marks_list.append(m)
    return analyse_student(name, marks_list)


# ── Main program ─────────────────────────────────────────────

print("=" * 55)
print("          STUDENT GRADE CALCULATOR")
print("=" * 55)
print(f"  Subjects : {', '.join(SUBJECTS)}")
print(f"  Max Marks: {MAX_MARKS} per subject")
print(f"  Pass Mark: {PASSING_MARKS} per subject")
print()
print("  GRADING SCALE:")
print("  90-100 -> A+ (Outstanding)  |  60-69 -> C (Average)")
print("  80-89  -> A  (Excellent)     |  50-59 -> D (Below Avg)")
print("  70-79  -> B  (Good)          |  <50   -> F (Fail)")
print("=" * 55)

all_students = []

while True:
    print()
    print(f"  Student #{len(all_students) + 1}")
    print("  " + "-" * 30)

    student_data = collect_student_data()
    all_students.append(student_data)
    display_result_card(student_data)

    print()
    add_more = input("  Add another student? (yes/no): ").strip().lower()
    if add_more not in ("yes", "y"):
        break

# ── Class summary (if more than one student) ─────────────────
if len(all_students) > 1:
    print()
    print("=" * 55)
    print("              CLASS SUMMARY")
    print("=" * 55)

    percentages = [s["percentage"] for s in all_students]
    class_avg   = sum(percentages) / len(percentages)
    top_student = max(all_students, key=lambda s: s["percentage"])
    low_student = min(all_students, key=lambda s: s["percentage"])
    pass_count  = sum(1 for s in all_students if s["status"] == "PASS")
    fail_count  = len(all_students) - pass_count

    print(f"  Total Students  : {len(all_students)}")
    print(f"  Class Average   : {class_avg:.2f}%")
    print(f"  Passed          : {pass_count}")
    print(f"  Failed          : {fail_count}")
    print(f"  Top Student     : {top_student['name']} ({top_student['percentage']:.2f}%)")
    print(f"  Lowest Scorer   : {low_student['name']} ({low_student['percentage']:.2f}%)")
    print()
    print(f"  {'#':<4} {'Name':<20} {'Pct%':>6} {'Grade':>6} {'Status':>6}")
    print("  " + "-" * 48)
    for i, s in enumerate(sorted(all_students, key=lambda x: x["percentage"], reverse=True), 1):
        print(f"  {i:<4} {s['name']:<20} {s['percentage']:>5.1f}% {s['grade']:>6} {s['status']:>6}")
    print("=" * 55)

print()
print("  Thank you for using the Grade Calculator!")

# ============================================================
# EXPECTED OUTPUT SAMPLE:
#   Enter student name:           (blank) -> [!] Name cannot be empty.
#   Enter marks for Mathematics:  abc     -> [!] Invalid input.
#   Enter marks for Mathematics:  -5      -> [!] Marks must be between 0 and 100.
#   Enter marks for Mathematics:  85
#   ...
#   RESULT: ** PASS **   Grade: A (Excellent)
# ============================================================
