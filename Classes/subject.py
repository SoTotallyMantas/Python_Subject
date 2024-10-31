class subject:
    def __init__(self,name,credits):
        self.name = name
        self.credits = credits
    def print_self(self):
        print( "Subject:", self.name, "\n",
              "Subject Credits:",self.credits)