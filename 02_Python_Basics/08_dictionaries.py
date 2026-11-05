import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# FILE: 08_dictionaries.py
# TOPIC: Dictionaries in Python
# ============================================================
#
# WHAT IS A DICTIONARY?
# A dictionary stores data as KEY : VALUE pairs.
# Each key is unique and is used to look up its value â€”
# just like a real dictionary where you look up a word (key)
# to find its definition (value).
#
# SYNTAX:
#   my_dict = {
#       "key1": value1,
#       "key2": value2
#   }
#
# KEY FEATURES:
#   - Keys must be unique
#   - Keys are usually strings or numbers
#   - Values can be any type (string, int, list, even another dict)
#   - Dictionaries are MUTABLE (can be changed after creation)
#   - Ordered (maintains insertion order, Python 3.7+)
# ============================================================

print("=" * 55)
print("         DICTIONARIES IN PYTHON")
print("=" * 55)

# -----------------------------------------------------------
# 1. CREATING A DICTIONARY
# -----------------------------------------------------------
print("\n--- 1. Creating a Dictionary ---")

# Student profile as a dictionary
student = {
    "name"    : "Alice Johnson",
    "age"     : 20,
    "course"  : "Computer Science",
    "marks"   : 88.5,
    "is_active": True
}

print("  Student dictionary:")
print(" ", student)

# An empty dictionary
empty_dict = {}
print("  Empty dict:", empty_dict)

# -----------------------------------------------------------
# 2. ACCESSING VALUES
# -----------------------------------------------------------
print("\n--- 2. Accessing Values ---")

# Access by key using square brackets
print("  Name   :", student["name"])
print("  Age    :", student["age"])
print("  Course :", student["course"])
print("  Marks  :", student["marks"])

# Using .get() â€” safer (returns None if key doesn't exist)
print("  Marks (get)  :", student.get("marks"))
print("  Phone (get)  :", student.get("phone"))            # key doesn't exist
print("  Phone (default):", student.get("phone", "N/A"))   # custom default

# -----------------------------------------------------------
# 3. ADDING AND UPDATING VALUES
# -----------------------------------------------------------
print("\n--- 3. Adding and Updating Values ---")

print("  Before:", student)

student["email"] = "alice@example.com"   # Add new key-value
student["age"] = 21                      # Update existing value

print("  After adding email and updating age:")
print(" ", student)

# -----------------------------------------------------------
# 4. REMOVING ITEMS
# -----------------------------------------------------------
print("\n--- 4. Removing Items ---")

temp_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print("  Original   :", temp_dict)

removed = temp_dict.pop("b")             # Remove key "b", returns value
print(f"  After pop('b'): {temp_dict}  | Removed value: {removed}")

del temp_dict["d"]                       # Delete key "d"
print("  After del['d']:", temp_dict)

# -----------------------------------------------------------
# 5. DICTIONARY METHODS
# -----------------------------------------------------------
print("\n--- 5. Dictionary Methods ---")

person = {
    "name"  : "Bob",
    "city"  : "Mumbai",
    "score" : 92
}

# .keys() â†’ all keys
print("  Keys   :", list(person.keys()))

# .values() â†’ all values
print("  Values :", list(person.values()))

# .items() â†’ all key-value pairs as tuples
print("  Items  :", list(person.items()))

# "in" operator â†’ check if a key exists
print()
print("  'name' in person   :", "name" in person)
print("  'email' in person  :", "email" in person)

# len() â†’ number of key-value pairs
print("  Number of entries  :", len(person))

# -----------------------------------------------------------
# 6. LOOPING THROUGH A DICTIONARY
# -----------------------------------------------------------
print("\n--- 6. Looping Through a Dictionary ---")

country_capitals = {
    "India"         : "New Delhi",
    "United States" : "Washington D.C.",
    "United Kingdom": "London",
    "Japan"         : "Tokyo",
    "France"        : "Paris"
}

print("  Country â†’ Capital:")
for country, capital in country_capitals.items():
    print(f"    {country:<20} â†’ {capital}")

# -----------------------------------------------------------
# 7. NESTED DICTIONARY
# -----------------------------------------------------------
print("\n--- 7. Nested Dictionary ---")

# A dictionary where values are also dictionaries
classroom = {
    "student1": {
        "name"   : "Alice",
        "marks"  : 88,
        "grade"  : "A"
    },
    "student2": {
        "name"   : "Bob",
        "marks"  : 72,
        "grade"  : "B"
    },
    "student3": {
        "name"   : "Charlie",
        "marks"  : 45,
        "grade"  : "F"
    }
}

print("  Classroom Report:")
for student_id, info in classroom.items():
    print(f"  {student_id}: {info['name']:<10} | "
          f"Marks: {info['marks']} | Grade: {info['grade']}")

# Access nested value
print("\n  Alice's marks:", classroom["student1"]["marks"])

# -----------------------------------------------------------
# 8. PRACTICAL EXAMPLE â€” Word Frequency Counter
# -----------------------------------------------------------
print("\n--- 8. Word Frequency Counter ---")

sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()      # split sentence into list of words

word_count = {}               # empty dictionary to store counts

for word in words:
    if word in word_count:
        word_count[word] += 1     # increment existing count
    else:
        word_count[word] = 1      # first occurrence

print("  Sentence :", sentence)
print("  Word Frequencies:")
for word, count in sorted(word_count.items()):
    print(f"    '{word}': {count}")

# -----------------------------------------------------------
# 9. DICTIONARY FROM TWO LISTS (using zip)
# -----------------------------------------------------------
print("\n--- 9. Creating Dictionary from Two Lists ---")

subjects = ["Maths", "Science", "English", "History", "Computer"]
scores   = [88, 75, 92, 68, 95]

# zip() pairs up items from both lists
subject_scores = dict(zip(subjects, scores))

print("  Subject Scores:")
for subject, score in subject_scores.items():
    status = "Pass" if score >= 50 else "Fail"
    print(f"    {subject:<10}: {score}  ({status})")

print("\n  Best subject:", max(subject_scores, key=subject_scores.get))
print("  Weak subject:", min(subject_scores, key=subject_scores.get))

# -----------------------------------------------------------
# 10. UPDATE AND COPY
# -----------------------------------------------------------
print("\n--- 10. update() and copy() ---")

defaults = {"font": "Arial", "size": 12, "colour": "Black"}
overrides = {"size": 14, "colour": "Blue"}

defaults.update(overrides)     # merge overrides into defaults
print("  After update:", defaults)

original = {"x": 1, "y": 2}
clone = original.copy()        # shallow copy
clone["x"] = 99
print("  Original (unchanged):", original)
print("  Clone (modified)    :", clone)

print("\n" + "=" * 55)
print("  DICTIONARY QUICK REFERENCE:")
print("=" * 55)
print("  d[key]          â†’ Get value")
print("  d[key] = val    â†’ Set/update value")
print("  d.get(key, def) â†’ Safe get with default")
print("  d.keys()        â†’ All keys")
print("  d.values()      â†’ All values")
print("  d.items()       â†’ All key-value pairs")
print("  key in d        â†’ Check if key exists")
print("  d.pop(key)      â†’ Remove and return value")
print("  d.update(other) â†’ Merge another dict in")
print("=" * 55)

