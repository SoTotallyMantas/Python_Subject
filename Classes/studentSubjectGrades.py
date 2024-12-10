from Classes.grades import Grades

class StudentSubjectGrades:
    def __init__(self, subject, grades):
        self.subject = subject
        self.grades = grades if isinstance(grades, Grades) else Grades(grades)

    def average_grades(self):
        return self.grades.average_grade()

    def print_self(self):
        print(f"\nSubject: {self.subject.name}, Credits: {self.subject.credits}")
        self.grades.print_self()
        print(f"Average Grade: {self.average_grades():.2f}")