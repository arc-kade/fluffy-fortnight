"""Student Record Management System (Week 4)

Concepts used: list & nested list, list comprehension, strings,
dictionary with zip(), tuple, set, shallow copy, deep copy, error handling.
"""

import copy

SUBJECTS = 3


def read_int(prompt, minimum=None, maximum=None):
    """Keep asking until the user enters a valid whole number in range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"  Value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"  Value must be at most {maximum}.")
            continue
        return value


def read_name(prompt):
    """Keep asking until the user enters a non-empty name."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("  Name cannot be empty.")


def collect_students():
    """Read all student data and return (names, rolls, marks)."""
    count = read_int("Enter the number of students: ", minimum=1)

    names = []   # list of strings
    rolls = []   # list of ints
    marks = []   # nested list: one inner list per student

    for i in range(1, count + 1):
        print(f"\n--- Student {i} ---")
        names.append(read_name("Name: "))

        while True:
            roll = read_int("Roll number: ", minimum=1)
            if roll in rolls:
                print("  That roll number already exists. Try another.")
            else:
                rolls.append(roll)
                break

        student_marks = [
            read_int(f"Marks in subject {s} (0-100): ", minimum=0, maximum=100)
            for s in range(1, SUBJECTS + 1)
        ]
        marks.append(student_marks)

    return names, rolls, marks


def show_dictionary(rolls, names):
    print("\n=== Roll Number -> Name (zip) ===")
    roll_name_dict = dict(zip(rolls, names))
    print(roll_name_dict)


def string_operations(names):
    print("\n=== String Operations ===")
    upper_names = [n.upper() for n in names]
    print("Uppercase names:", upper_names)

    long_names = [n for n in names if len(n) > 5]
    print("Names longer than 5 characters:", long_names)

    a_count = sum(1 for n in names if n.upper().startswith("A"))
    print("Names starting with 'A':", a_count)


def list_comprehensions(names, rolls, marks):
    print("\n=== List Comprehensions ===")
    high_scorers = [
        name for name, m in zip(names, marks) if sum(m) / len(m) > 75
    ]
    print("Students with average marks > 75:", high_scorers)

    even_rolls = [r for r in rolls if r % 2 == 0]
    print("Even roll numbers:", even_rolls)


def tuple_and_set(marks):
    print("\n=== Tuple and Set ===")
    first_marks = tuple(marks[0])
    print("First student's marks (tuple):", first_marks)

    unique_marks = {m for student in marks for m in student}
    print("Unique marks of all students (set):", unique_marks)


def copy_demo(marks):
    print("\n=== Shallow Copy vs Deep Copy ===")
    shallow = copy.copy(marks)       # new outer list, SAME inner lists
    deep = copy.deepcopy(marks)      # fully independent copy

    # Modify one student's mark in the original list
    marks[0][0] += 1
    print("(Changed first student's first mark in the original)\n")

    print("Original  :", marks)
    print("Shallow   :", shallow, " <- inner lists are shared, so it changed")
    print("Deep copy :", deep, " <- independent, unchanged")


def main():
    print("=== Student Record Management System ===\n")
    try:
        names, rolls, marks = collect_students()
    except (EOFError, KeyboardInterrupt):
        print("\nInput was cancelled. Exiting.")
        return
    except Exception as error:
        print(f"\nUnexpected error while reading input: {error}")
        return

    try:
        show_dictionary(rolls, names)
        string_operations(names)
        list_comprehensions(names, rolls, marks)
        tuple_and_set(marks)
        copy_demo(marks)
    except Exception as error:
        print(f"\nSomething went wrong while processing the data: {error}")


if __name__ == "__main__":
    main()