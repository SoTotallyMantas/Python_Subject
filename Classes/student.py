from Classes.studentSubjectGrades import StudentSubjectGrades
from Classes.basePerson import Person


class Student(Person):
    def __init__(self, fname, lname, age, financingstatus):
        super().__init__(fname, lname, age)
        self.subject_grades = []
        self.financingstatus = financingstatus

    def add_subject_grade(self, student_subject_grades):
        self.subject_grades.append(student_subject_grades)

    def average_grade(self):
        total_grades = [subject_grade.average_grades() for subject_grade in self.subject_grades]
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def print_self(self):
        print(f"\nStudent: {self.firstname} {self.lastname}")
        print(f"Age: {self.age}, Financing: {self.financingstatus}")
        for subject_grade in self.subject_grades:
            subject_grade.print_self()