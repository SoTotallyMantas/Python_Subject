from Classes.base_person import person

class teacher(person):
   
    def __init__(self,fname,lname,age,pay):
        super().__init__(fname,lname,age)
        self.pay = pay
        self.subjects = []
    def add_subject(self,subject):
        self.subjects.append(subject)

    def remove_subject(self,subject):
        self.subjects.remove(subject)

    def print_self(self):
        print("Teacher FirstName:",self.firstname, "\n",
              "Teacher LastName:", self.lastname, "\n",
              "Teacher Age:",self.age, "\n",
              "Teacher Pay:",self.pay, "\n",)
        for subject in self.subjects:
            subject.print_self()