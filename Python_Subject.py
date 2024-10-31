



from tkinter.filedialog import SaveAs
from Classes.group import group
from Classes.program import program
from Classes.subject import subject
from Classes.teacher import teacher
from Classes.student import student
from Classes.grades import grades
from Classes.student_subject_grades import student_subject_grades
from Utilities.FileOperations import saveToFile
from Utilities.FileOperations import readFromFile
from Utilities.formatToJSON import JSONFormater


program1 = program("Computer Science")
year1 = 1
year2 = 2
group1 = group("A",year1)
group2 = group("B",year2)
subject1 = subject("Math",5)
subject2 = subject("Programming",5)
subject3 = subject("English",3)
grades1 = grades([5,4,3,5,4])
grades2 = grades([3,4,5,4,5])
student1 = student("John","Doe",20,"self-financed")
student2 = student("Jane","Doe",25,"self-financed")

student_subject_grades1 = student_subject_grades(subject1,grades1)
student_subject_grades2 = student_subject_grades(subject1,grades2)
student1.add_subject_grade(student_subject_grades1)
student2.add_subject_grade(student_subject_grades2)


teacher1 = teacher("John","Smith",30,2000)
teacher2 = teacher("Jane","Smith",35,2500)

program1.add_group(group1)
program1.add_group(group2)
group1.add_student(student1)
group2.add_student(student2)
group1.add_subject(subject1)
group1.add_subject(subject3)
group2.add_subject(subject2)
group2.add_subject(subject3)
teacher1.add_subject(subject1)
teacher1.add_subject(subject2)
teacher2.add_subject(subject3)


program1.print_self()
teacher1.print_self()
teacher2.print_self()
Data = JSONFormater.ObjectToData(program1)
saveToFile("program1.txt",Data)
print(readFromFile("program1.txt"))




        

    
