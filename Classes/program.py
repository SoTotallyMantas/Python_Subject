
class program:
    def __init__(self,name):
        self.name = name
        self.groups = []

    def add_group(self,group):
        self.groups.append(group)
    def remove_group(self,group):
        self.groups.remove(group)

    def print_self(self):
        print(self.name)
        for group in self.groups:
            group.print_self()