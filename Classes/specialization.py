class Specialization:
    def __init__(self, name, grade_threshold):
        self.name = name
        self.grade_threshold = grade_threshold
        self.students = []

    def assign_student(self, student):
        
        if student.average_grade() >= self.grade_threshold:
            self.students.append(student)

    def print_self(self):
        print(f"\nSpecialization: {self.name}")
        print(f"Grade Threshold: {self.grade_threshold}")
        print("Students:")
        for student in self.students:
            student.print_self()