import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 07_lists_and_tuples.py
# TOPIC: Lists and Tuples in Python
# ============================================================
#
# WHAT IS A LIST?
# A list is an ordered collection of items.
# Lists are MUTABLE â€” you can add, remove, or change items.
# Lists use square brackets: [item1, item2, item3]
#
# WHAT IS A TUPLE?
# A tuple is also an ordered collection of items.
# Tuples are IMMUTABLE â€” once created, they CANNOT be changed.
# Tuples use parentheses: (item1, item2, item3)
#
# KEY DIFFERENCE:
#   List  â†’ Changeable (like a shopping list you can edit)
#   Tuple â†’ Fixed (like GPS coordinates that don't change)
# ============================================================

print("=" * 55)
print("        LISTS AND TUPLES IN PYTHON")
print("=" * 55)

# ============================================================
# PART A: LISTS
# ============================================================
print("\n" + "=" * 55)
print("  PART A: LISTS")
print("=" * 55)

# -----------------------------------------------------------
# 1. CREATING A LIST
# -----------------------------------------------------------
print("\n--- 1. Creating Lists ---")

# A list of student names
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# A list of numbers
marks = [85, 92, 78, 65, 90]

# A mixed list (different types)
mixed = ["Alice", 20, 85.5, True]

# An empty list
empty_list = []

print("  Students list :", students)
print("  Marks list    :", marks)
print("  Mixed list    :", mixed)
print("  Empty list    :", empty_list)
print("  Number of students:", len(students))   # len() gives list length

# -----------------------------------------------------------
# 2. ACCESSING LIST ITEMS (Indexing)
# -----------------------------------------------------------
print("\n--- 2. Indexing (Accessing Items) ---")
print("  Index:  0      1       2        3     4")
print(" ", students)
print()

# Positive indexing (starts from 0)
print("  students[0]  â†’", students[0])    # First item
print("  students[2]  â†’", students[2])    # Third item
print("  students[4]  â†’", students[4])    # Fifth item

# Negative indexing (starts from -1 at the end)
print("  students[-1] â†’", students[-1])   # Last item
print("  students[-2] â†’", students[-2])   # Second to last

# -----------------------------------------------------------
# 3. SLICING â€” Getting a portion of the list
# -----------------------------------------------------------
print("\n--- 3. Slicing Lists ---")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("  Full list :", numbers)

print("  [0:4]     â†’", numbers[0:4])    # index 0, 1, 2, 3 (not 4)
print("  [3:7]     â†’", numbers[3:7])    # index 3, 4, 5, 6
print("  [:5]      â†’", numbers[:5])     # first 5 items
print("  [5:]      â†’", numbers[5:])     # from index 5 to end
print("  [::2]     â†’", numbers[::2])    # every 2nd item
print("  [::-1]    â†’", numbers[::-1])   # reversed list

# -----------------------------------------------------------
# 4. MODIFYING A LIST
# -----------------------------------------------------------
print("\n--- 4. Modifying List Items ---")

colours = ["Red", "Green", "Blue"]
print("  Original :", colours)

colours[1] = "Yellow"           # Change item at index 1
print("  After colours[1]='Yellow' :", colours)

# -----------------------------------------------------------
# 5. LIST METHODS
# -----------------------------------------------------------
print("\n--- 5. List Methods ---")

fruits = ["Apple", "Banana", "Cherry"]
print("  Initial list:", fruits)

fruits.append("Mango")           # Add to END
print("  After append('Mango')  :", fruits)

fruits.insert(1, "Blueberry")    # Insert at position 1
print("  After insert(1,'Blueberry'):", fruits)

fruits.remove("Banana")          # Remove by value
print("  After remove('Banana'):", fruits)

popped = fruits.pop()            # Remove and return last item
print("  After pop()            :", fruits, "| Removed:", popped)

fruits.sort()                    # Sort alphabetically
print("  After sort()           :", fruits)

fruits.reverse()                 # Reverse the list
print("  After reverse()        :", fruits)

print("  Count of 'Apple'       :", fruits.count("Apple"))
print("  Index of 'Cherry'      :", fruits.index("Cherry"))

# -----------------------------------------------------------
# 6. LOOPING THROUGH A LIST
# -----------------------------------------------------------
print("\n--- 6. Looping Through a List ---")

subjects = ["Maths", "Science", "English", "History", "Computer"]
marks_list = [88, 75, 92, 68, 95]

print("  Subject Results:")
for i in range(len(subjects)):
    status = "âœ“ Pass" if marks_list[i] >= 50 else "âœ— Fail"
    print(f"  {i+1}. {subjects[i]:<10} : {marks_list[i]} marks  {status}")

# -----------------------------------------------------------
# 7. LIST FUNCTIONS â€” min, max, sum
# -----------------------------------------------------------
print("\n--- 7. Useful List Functions ---")

scores = [78, 92, 55, 88, 73, 96, 45, 83]
print("  Scores    :", scores)
print("  Minimum   :", min(scores))
print("  Maximum   :", max(scores))
print("  Total Sum :", sum(scores))
print("  Average   :", sum(scores) / len(scores))
print("  Count     :", len(scores))
print("  Sorted    :", sorted(scores))          # sorted() returns new list

# ============================================================
# PART B: TUPLES
# ============================================================
print("\n" + "=" * 55)
print("  PART B: TUPLES")
print("=" * 55)

# -----------------------------------------------------------
# 8. CREATING A TUPLE
# -----------------------------------------------------------
print("\n--- 8. Creating Tuples ---")

# Tuples use parentheses
coordinates = (28.6139, 77.2090)          # Delhi's GPS coordinates
rgb_red = (255, 0, 0)                     # RGB colour â€” fixed values
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

print("  Coordinates :", coordinates)
print("  RGB Red     :", rgb_red)
print("  Days        :", days)
print("  Number of days:", len(days))

# -----------------------------------------------------------
# 9. ACCESSING TUPLE ITEMS
# -----------------------------------------------------------
print("\n--- 9. Accessing Tuple Items ---")

print("  First day  :", days[0])
print("  Last day   :", days[-1])
print("  Weekdays   :", days[:5])    # slicing works on tuples too
print("  Weekend    :", days[5:])

# -----------------------------------------------------------
# 10. TUPLES ARE IMMUTABLE
# -----------------------------------------------------------
print("\n--- 10. Tuples are Immutable ---")
print("  Trying to change a tuple causes a TypeError:")
print("  >>> rgb_red[0] = 100  â† This would raise TypeError!")
print("  (We don't execute it, just showing it would fail)")

# -----------------------------------------------------------
# 11. TUPLE UNPACKING
# -----------------------------------------------------------
print("\n--- 11. Tuple Unpacking ---")

# Assign tuple values to individual variables at once
latitude, longitude = (28.6139, 77.2090)
print(f"  Latitude : {latitude}")
print(f"  Longitude: {longitude}")

first, *middle, last = (1, 2, 3, 4, 5)
print(f"  First: {first}, Middle: {middle}, Last: {last}")

# -----------------------------------------------------------
# 12. LIST VS TUPLE SUMMARY
# -----------------------------------------------------------
print("\n--- 12. List vs Tuple ---")
print()
print("  Feature          | List          | Tuple")
print("  " + "-" * 45)
print("  Brackets         | [  ]          | (  )")
print("  Mutable?         | YES (change)  | NO (fixed)")
print("  Speed            | Slightly slow | Faster")
print("  Use when...      | Data changes  | Data is constant")
print("  Example          | student marks | GPS coordinates")

print("\n" + "=" * 55)
print("  KEY METHODS FOR LISTS:")
print("=" * 55)
print("  append(x)   â†’ Add x to the end")
print("  insert(i,x) â†’ Insert x at index i")
print("  remove(x)   â†’ Remove first occurrence of x")
print("  pop()       â†’ Remove and return last item")
print("  sort()      â†’ Sort in place")
print("  reverse()   â†’ Reverse in place")
print("  len(list)   â†’ Number of items")
print("=" * 55)

