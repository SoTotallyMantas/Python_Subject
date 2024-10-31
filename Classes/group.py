class group:
    def __init__(self,name,year):
        self.name = name
        self.students = []
        self.subjects = []
        self.currentYear = year


    def add_student(self,student):
        self.students.append(student)
    def remove_student(self,student):
        self.students.remove(student)


    def add_subject (self,subject):
        self.subjects.append(subject)
    def remove_subject(self,subject):
        self.subjects.remove(subject)
    
    def print_self(self):
        print("Group Name:", self.name , "\n",)
        for student in self.students:
            student.print_self()
        for subject in self.subjects:
            subject.print_self()
        print("Student Group Current Year:",self.currentYear)
