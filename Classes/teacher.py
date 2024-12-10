from Classes.basePerson import Person

class Teacher(Person):
    def __init__(self, fname, lname, age, pay):
        super().__init__(fname, lname, age)
        self.pay = pay
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

    def print_self(self):
        print(f"\nTeacher: {self.firstname} {self.lastname}")
        print(f"Age: {self.age}, Pay: {self.pay}")
        for subject in self.subjects:
            subject.print_self()