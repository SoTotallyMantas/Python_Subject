class Subject:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def print_self(self):
        print(f"Subject: {self.name}, Credits: {self.credits}")

