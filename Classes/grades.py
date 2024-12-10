


class Grades:
    def __init__(self, outergrade):
        self.grade = [] if outergrade == None else outergrade

    def __len__(self):
        return len(self.grade)

    def average_grade(self):
        return sum(self.grade) / len(self.grade) if len(self.grade) > 0 else 0
    def print_self(self):
        print("Grades: " + ", ".join(map(str, self.grade)))


