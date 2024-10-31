
from asyncio.windows_events import NULL


class grades:
   
    def __init__(self,outergrade):
        if(outergrade == NULL):
            self.grade = []
        else:
          self.grade = outergrade

    def __len__(self):
      return len(self.grade)
    

    def print_self(self):
        for gradesingle in self.grade:
            print("Grade:",gradesingle)
