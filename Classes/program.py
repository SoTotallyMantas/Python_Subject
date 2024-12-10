
class Program:
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.specializations = []

    def add_group(self, group):
        self.groups.append(group)

    def remove_group(self, group):
        self.groups.remove(group)
    def add_specialization(self, specialization):
        self.specializations.append(specialization)

    def remove_specialization(self, specialization):
        self.specializations.remove(specialization)

    def assign_students_to_specializations(self):
        # For visus studentus ir paskirstome i pirma pasiekta specializacija
        for group in self.groups:
            for student in group.students:
                assigned = False
                for specialization in self.specializations:  # For visus specializacijas
                    if student.average_grade() >= specialization.grade_threshold:  # Jei studento vidurkis didesnis arba lygus specializacijos reikalavimui
                        specialization.assign_student(student) 
                        assigned = True
                        break # stabdom , kad nepriskirti kitai specializacijai
                if not assigned:
                    print(f"Student {student.firstname} {student.lastname} has not been assigned to any specialization")
    def print_self(self):
        print(f"\nProgram: {self.name}")
        for group in self.groups:
            group.print_self()