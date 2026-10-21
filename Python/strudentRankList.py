"""Student Rank List Management System

OOP concepts demonstrated: constructors, encapsulation, inheritance,
multiple inheritance, abstraction, polymorphism, operator overloading,
static method, class method, and rank preparation using a list of objects.
"""

from abc import ABC, abstractmethod
from functools import total_ordering

SUBJECTS = 3


# ---------------------------------------------------------------- Abstraction
class Evaluation(ABC):
    """Abstract class: every evaluated entity must define a grade."""

    @abstractmethod
    def calculate_grade(self):
        pass


# -------------------------------------------------------------- Encapsulation
class Person:
    """Base class with private attributes exposed through getters."""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# ---------------------------------------------------------------- Inheritance
@total_ordering
class Student(Person, Evaluation):
    """Student is a Person and implements the Evaluation contract."""

    _total_students = 0   # class-level counter

    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        if len(marks) != SUBJECTS or not all(Student.validate_marks(m) for m in marks):
            raise ValueError(f"Marks must be {SUBJECTS} values between 0 and 100.")
        self.roll_no = roll_no
        self.marks = list(marks)
        Student._total_students += 1

    # ---- static method
    @staticmethod
    def validate_marks(mark):
        """Return True only for an integer between 0 and 100."""
        return isinstance(mark, int) and 0 <= mark <= 100

    # ---- class method
    @classmethod
    def get_total_students(cls):
        return Student._total_students

    @classmethod
    def display_total_students(cls):
        print(f"Total number of students created: {cls.get_total_students()}")

    # ---- calculations
    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def calculate_grade(self):
        avg = self.average_marks()
        if avg >= 90:
            return "A+"
        if avg >= 80:
            return "A"
        if avg >= 70:
            return "B"
        if avg >= 60:
            return "C"
        if avg >= 50:
            return "D"
        return "F"

    def ranking_key(self):
        """What the rank list is sorted on. Subclasses may extend it."""
        return (self.total_marks(),)

    # ---- operator overloading (total_ordering fills in >, <=, >=)
    def __lt__(self, other):
        return self.ranking_key() < other.ranking_key()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.ranking_key() == other.ranking_key()

    __hash__ = None  # objects are mutable and compared by value

    # ---- display (overridden in Result -> polymorphism)
    def display_details(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.get_name()}  (Age: {self.get_age()})")
        print(f"Marks   : {self.marks}")
        print(f"Total   : {self.total_marks()}")
        print(f"Average : {self.average_marks():.2f}")
        print(f"Grade   : {self.calculate_grade()}")


class Sports:
    """Independent class holding a sports score."""

    def __init__(self, sports_score):
        if not Student.validate_marks(sports_score):
            raise ValueError("Sports score must be between 0 and 100.")
        self.sports_score = sports_score

    def display_sports(self):
        print(f"Sports  : {self.sports_score}")


# ------------------------------------------------------ Multiple inheritance
class Result(Student, Sports):
    """Final result: academic details plus sports score.

    Rank is decided by total marks first; the sports score breaks ties.
    """

    def __init__(self, name, age, roll_no, marks, sports_score):
        Student.__init__(self, name, age, roll_no, marks)
        Sports.__init__(self, sports_score)

    def ranking_key(self):
        return (self.total_marks(), self.sports_score)

    def display_details(self):          # polymorphism: overrides Student's
        super().display_details()
        self.display_sports()


# ------------------------------------------------------------------- Helpers
def read_int(prompt, minimum=None, maximum=None):
    """Keep asking until a whole number in range is entered."""
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
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("  Name cannot be empty.")


def read_student(index, used_rolls):
    print(f"\n--- Student {index} ---")
    name = read_name("Name: ")
    age = read_int("Age: ", minimum=1, maximum=120)

    while True:
        roll = read_int("Roll number: ", minimum=1)
        if roll in used_rolls:
            print("  That roll number already exists. Try another.")
        else:
            used_rolls.add(roll)
            break

    marks = [
        read_int(f"Marks in subject {s} (0-100): ", minimum=0, maximum=100)
        for s in range(1, SUBJECTS + 1)
    ]
    sports = read_int("Sports score (0-100): ", minimum=0, maximum=100)
    return Result(name, age, roll, marks, sports)


def print_rank_list(students):
    ranked = sorted(students, reverse=True)   # uses __lt__ via total_ordering
    print("\n" + "=" * 62)
    print(f"{'Rank':<6}{'Roll':<8}{'Name':<18}{'Total':<8}{'Avg':<8}{'Sports':<8}{'Grade'}")
    print("-" * 62)
    for rank, s in enumerate(ranked, start=1):
        print(f"{rank:<6}{s.roll_no:<8}{s.get_name():<18}{s.total_marks():<8}"
              f"{s.average_marks():<8.2f}{s.sports_score:<8}{s.calculate_grade()}")
    print("=" * 62)


def main():
    print("=== Student Rank List Management System ===\n")
    try:
        n = read_int("Enter the number of students (N): ", minimum=1)

        students = []           # list of objects
        used_rolls = set()
        for i in range(1, n + 1):
            students.append(read_student(i, used_rolls))

        print("\n########## STUDENT DETAILS ##########")
        for s in students:
            print()
            s.display_details()

        print("\n########## RANK LIST ##########")
        print_rank_list(students)

        print()
        Student.display_total_students()

    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. Exiting.")
    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()