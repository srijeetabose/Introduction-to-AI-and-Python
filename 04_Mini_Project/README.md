# 🏆 Mini Project — Student Performance Analyzer

## Project Description

The **Student Performance Analyzer** is a menu-driven Python application that collects student marks across five subjects, computes performance metrics, assigns letter grades, and generates formatted reports.

> **Important Disclaimer:**  
> This application is a **Python programming exercise** — a data analysis tool built with core Python concepts.  
> It does **not** use Machine Learning, AI models, or any external libraries.  
> All computations are done using Python's standard arithmetic and logic.

---

## Features

| Feature | Description |
|---------|-------------|
| Add students | Enter name and marks for 1–50 students |
| Full class report | Ranked table of all students with totals, averages, grades |
| Individual report | Detailed card with subject-wise bar chart for one student |
| Edit marks | Re-enter marks for any student |
| Remove student | Delete a student record (with confirmation) |
| Search | Find students by partial name match |
| Class statistics | Highest scorer, lowest scorer, class average, pass rate |
| Input validation | Rejects blank names, non-numeric marks, out-of-range values |

---

## Subjects Assessed

1. Mathematics  
2. Science  
3. English  
4. History  
5. Computer Science  

Maximum marks per subject: **100**  
Minimum pass mark per subject: **50**  
Total maximum marks: **500**

---

## Grading Scale

| Percentage   | Grade | Remark         |
|--------------|-------|----------------|
| 90% – 100%  | A+    | Outstanding    |
| 80% – 89%   | A     | Excellent      |
| 70% – 79%   | B     | Good           |
| 60% – 69%   | C     | Average        |
| 50% – 59%   | D     | Below Average  |
| Below 50%   | F     | Fail           |

**Pass condition:** A student passes only if they score ≥ 50 in **every** subject.

---

## How to Run

```bash
cd 04_Mini_Project
python student_performance_analyzer.py
```

---

## Menu Options

```
+-------+------------------------------------------+
| MENU  |  STUDENT PERFORMANCE ANALYZER            |
+-------+------------------------------------------+
|  1    |  Add student(s)                          |
|  2    |  View full class report                  |
|  3    |  View individual student report          |
|  4    |  Edit student marks                      |
|  5    |  Remove a student                        |
|  6    |  Search student by name                  |
|  7    |  List all students                       |
|  0    |  Exit                                    |
+-------+------------------------------------------+
```

---

## Sample Session

### Adding a student

```
How many students do you want to add? 1
Student name: Alice
Enter marks for Alice:
  Mathematics   : 88
  Science       : 92
  English       : 75
  History       : 68
  Computer Sc.  : 95

Student 'Alice' added successfully.
Percentage: 83.60%  |  Grade: A  |  Status: PASS
```

### Input validation examples

```
Student name:               ← (blank)
[!] Name cannot be empty.

Mathematics: abc
[!] 'abc' is not a valid number.

Mathematics: 150
[!] Marks must be between 0 and 100.

Mathematics: -5
[!] Marks must be between 0 and 100.
```

### Individual student report

```
  Student   : Alice
  Grade     : A  (Excellent)
  Status    : PASS
  --------------------------------------------------------
  Subject          Marks/100   Subject Status
  --------------------------------------------------------
  Mathematics        88.0            Pass  [#################---]
  Science            92.0            Pass  [##################--]
  English            75.0            Pass  [###############-----]
  History            68.0            Pass  [#############-------]
  Computer Sc.       95.0            Pass  [###################-]
  --------------------------------------------------------
  Total              418.0/500
  Average             83.6
  Percentage          83.60%
```

### Full class report (3 students)

```
  No   Name                 Total    Avg%  Grade  Status
  --------------------------------------------------------
  1    Alice                  418   83.60%     A    PASS
  2    Bob                    367   73.40%     B    PASS
  3    Charlie                241   48.20%     F    FAIL
  --------------------------------------------------------
  Class Average  : 68.40%
  Highest Scorer : Alice (83.60%)
  Lowest Scorer  : Charlie (48.20%)
  Pass Rate      : 66.7%
```

---

## Python Concepts Demonstrated

- **Functions** — Separate functions for input, calculation, display, and menu
- **Dictionaries** — Each student stored as a dict with all their data
- **Lists** — All students in a master list
- **For loops** — Iterate over subjects and students
- **While loops** — Menu loop, input validation retry loop
- **if/elif/else** — Grade assignment, pass/fail logic
- **try/except** — Catches ValueError on non-numeric input
- **f-strings** — All formatted output
- **String methods** — .strip(), .lower() for input cleaning
- **Built-in functions** — sum(), max(), min(), sorted()

---

## Files

| File | Description |
|------|-------------|
| `student_performance_analyzer.py` | Main application — all code in one file |
| `README.md` | This documentation file |
