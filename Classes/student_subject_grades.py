
class student_subject_grades:
    def __init__(self,subject,grades):
        self.subject = subject
        self.grades = grades

    def average_grades(self):
        
        return sum(self.grades.grade) / len(self.grades)

    def print_self(self):
        
        self.subject.print_self()
        
        self.grades.print_self()
        print("Average Grade:", self.average_grades())