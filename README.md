# 🤖 Introduction to AI & Python

> A beginner-friendly learning module to understand Artificial Intelligence concepts and build a solid foundation in Python programming.

---

## 📌 Project Overview

This repository is a structured learning module designed for absolute beginners who want to understand what Artificial Intelligence is and learn Python programming from scratch. The project combines theory with hands-on coding exercises and a real mini-project — no prior programming experience required.

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:

1. ✅ Understand what Artificial Intelligence is and how it works
2. ✅ Explain the difference between AI, Machine Learning, and Deep Learning
3. ✅ Identify real-world applications of AI across industries
4. ✅ Write Python programs using core programming concepts
5. ✅ Build beginner-friendly Python applications from scratch

---

## 🛠️ Technologies Used

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Python 3.x  | Programming language             |
| Markdown    | Documentation and theory notes   |
| Git & GitHub| Version control and hosting      |

> **No external Python libraries are required.** All programs use Python's built-in standard library only.

---

## 📁 Project Folder Structure

```
Introduction-to-AI-and-Python/
│
├── README.md                          ← You are here
├── requirements.txt                   ← Dependencies (standard library only)
├── LICENSE                            ← MIT License
├── .gitignore                         ← Git ignore rules
│
├── 01_Introduction_to_AI/
│   ├── introduction_to_ai.md          ← What is AI? History, types, concepts
│   ├── ai_vs_ml_vs_dl.md              ← AI vs ML vs DL explained visually
│   └── real_world_ai_applications.md  ← AI in healthcare, finance, education, etc.
│
├── 02_Python_Basics/
│   ├── 01_hello_world.py              ← Your first Python program
│   ├── 02_variables_and_datatypes.py  ← Variables, int, float, str, bool
│   ├── 03_operators.py                ← Arithmetic, comparison, logical operators
│   ├── 04_conditional_statements.py   ← if, elif, else
│   ├── 05_for_loops.py                ← for loop patterns
│   ├── 06_while_loops.py              ← while loop patterns
│   ├── 07_lists_and_tuples.py         ← Lists and tuples
│   ├── 08_dictionaries.py             ← Dictionary operations
│   ├── 09_functions.py                ← Defining and calling functions
│   └── 10_user_input.py               ← Input, type conversion, interaction
│
├── 03_Python_Exercises/
│   ├── even_odd_checker.py            ← Check if a number is even or odd
│   ├── calculator.py                  ← Basic arithmetic calculator
│   ├── multiplication_table.py        ← Print multiplication table
│   ├── palindrome_checker.py          ← Check if a word is a palindrome
│   ├── number_guessing_game.py        ← Interactive number guessing game
│   └── student_grade_calculator.py    ← Calculate grades from marks
│
├── 04_Mini_Project/
│   ├── student_performance_analyzer.py ← Full menu-driven student analyzer
│   └── README.md                       ← Mini-project documentation
│
├── 05_Learning_Notes/
│   └── learning_notes.md              ← Comprehensive study notes
│
└── 06_Outputs/
    └── sample_outputs.md              ← Expected output from all programs
```

---

## ⚙️ Installation Instructions

### Step 1 — Install Python

Download and install Python 3.x from the official website:  
👉 https://www.python.org/downloads/

During installation on Windows, check **"Add Python to PATH"**.

### Step 2 — Verify Installation

Open your terminal (Command Prompt / PowerShell / Terminal) and run:

```bash
python --version
```

You should see something like `Python 3.11.x`.

### Step 3 — Clone the Repository

```bash
git clone https://github.com/your-username/Introduction-to-AI-and-Python.git
cd Introduction-to-AI-and-Python
```

Or download the ZIP from GitHub and extract it.

---

## ▶️ How to Run the Programs

### Python Basics

```bash
# Navigate to the Python Basics folder
cd 02_Python_Basics

python 01_hello_world.py
python 02_variables_and_datatypes.py
python 03_operators.py
python 04_conditional_statements.py
python 05_for_loops.py
python 06_while_loops.py
python 07_lists_and_tuples.py
python 08_dictionaries.py
python 09_functions.py
python 10_user_input.py
```

### Python Exercises

```bash
cd 03_Python_Exercises

python even_odd_checker.py
python calculator.py
python multiplication_table.py
python palindrome_checker.py
python number_guessing_game.py
python student_grade_calculator.py
```

### Mini Project

```bash
cd 04_Mini_Project
python student_performance_analyzer.py
```

---

## 🏆 Mini Project — Student Performance Analyzer

The **Student Performance Analyzer** is a menu-driven Python application that:

- Accepts multiple student names and their marks in 5 subjects
- Calculates each student's total marks and average percentage
- Determines letter grades (A+, A, B, C, D, F) based on percentage
- Identifies pass or fail status
- Finds the highest and lowest scoring students
- Calculates the overall class average
- Displays a neatly formatted performance report

> ⚠️ **Disclaimer:** This is a Python-based data analysis application. It does **not** use Machine Learning, AI models, or any external libraries. It is purely a Python programming exercise.

**Grading Scale Used:**

| Percentage  | Grade | Status |
|-------------|-------|--------|
| 90% – 100%  | A+    | Pass   |
| 80% – 89%   | A     | Pass   |
| 70% – 79%   | B     | Pass   |
| 60% – 69%   | C     | Pass   |
| 50% – 59%   | D     | Pass   |
| Below 50%   | F     | Fail   |

---

## 📊 Sample Output

```
========================================
    STUDENT PERFORMANCE ANALYZER
========================================

Enter number of students: 3
Enter student 1 name: Alice
  Subject 1 marks: 85
  Subject 2 marks: 90
  Subject 3 marks: 78
  Subject 4 marks: 92
  Subject 5 marks: 88

...

============================================================
              STUDENT PERFORMANCE REPORT
============================================================
 No | Name       | Total | Average |Grade| Status
----+------------+-------+---------+-----+--------
  1 | Alice      |  433  |  86.60% |  A  | PASS
  2 | Bob        |  367  |  73.40% |  B  | PASS
  3 | Charlie    |  241  |  48.20% |  F  | FAIL
----+------------+-------+---------+-----+--------

Class Average: 69.40%
Highest Scorer: Alice (86.60%)
Lowest Scorer:  Charlie (48.20%)
```

---

## 🎓 Learning Outcomes

After completing this module you will have:

- A clear conceptual understanding of AI, ML, and Deep Learning
- Hands-on experience writing Python programs from scratch
- The ability to use variables, loops, conditions, functions, lists, and dictionaries
- A completed mini-project to add to your portfolio
- The foundation needed to move on to data science and machine learning

---

## 📚 Suggested Next Steps

Once you've completed this module, explore:

1. **Python for Data Science** — NumPy, Pandas, Matplotlib
2. **Machine Learning** — Scikit-learn
3. **Deep Learning** — TensorFlow or PyTorch
4. **Projects** — Build your own ML models

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

Built as part of the *Introduction to AI & Python* learning module.  
Designed to be accessible, practical, and beginner-friendly.

---

*Happy Learning! 🚀*
