from Classes.base_person import person


class student(person):

    def __init__(self,fname,lname,age,financingstatus):
        super().__init__(fname,lname,age)
        self.subject_grades = []
        self.financingstatus = financingstatus

    def add_subject_grade(self,student_subject_grades):
        self.subject_grades.append(student_subject_grades)
    
    def print_self(self):
      print("Student First Name:",self.firstname, "\n",
            "Student Last Name:",self.lastname, "\n",
            "Student Age:",self.age, "\n",
            "Financing:",self.financingstatus, "\n",)
      for subject_grade in self.subject_grades:
            subject_grade.print_self()