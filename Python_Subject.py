from Classes.group import Group
from Classes.program import Program
from Classes.subject import Subject
from Classes.teacher import Teacher
from Classes.student import Student
from Classes.grades import Grades
from Classes.studentSubjectGrades import StudentSubjectGrades
from Classes.specialization import Specialization
import json
import re
# Apskaiciuojame bendra vidurki
def calcTotalAverageGrade(program):
    total_grades = [student.average_grade() for group in program.groups for student in group.students if group.students]
    return sum(total_grades) / len(total_grades)


def createTest():
#----------------------------------------------
    subject_math = Subject("Math", 5)
    subject_programming = Subject("Programming", 5)
    subject_english = Subject("English", 3)


#----------------------------------------------
    student_john = Student("John", "Doe", 20, "self-financed")
    student_jane = Student("Jane", "Doe", 25, "self-financed")

#----------------------------------------------
    grades_john = Grades([5, 4, 5, 5, 4])
    grades_jane = Grades([3, 4, 5, 4, 5])

#----------------------------------------------
    student_subject_grades_john = StudentSubjectGrades(subject_math, grades_john)
    student_subject_grades_jane = StudentSubjectGrades(subject_math, grades_jane)


#----------------------------------------------
    student_john.add_subject_grade(student_subject_grades_john)
    student_jane.add_subject_grade(student_subject_grades_jane)


#----------------------------------------------
    teacher_john = Teacher("John", "Smith", 30, 2000)
    teacher_jane = Teacher("Jane", "Smith", 35, 2500)


#----------------------------------------------
    group_a = Group("A", 1)
    group_b = Group("B", 2)


#----------------------------------------------
    group_a.add_student(student_john)
    group_b.add_student(student_jane)

#----------------------------------------------
    group_a.add_subject(subject_math)
    group_a.add_subject(subject_english)
    group_b.add_subject(subject_programming)
    group_b.add_subject(subject_english)

#----------------------------------------------
    teacher_john.add_subject(subject_math)
    teacher_john.add_subject(subject_programming)
    teacher_jane.add_subject(subject_english)


#----------------------------------------------
    program_computer_science = Program("Computer Science")
    program_computer_science.add_group(group_a)
    program_computer_science.add_group(group_b)


#----------------------------------------------
    program_computer_science.print_self()
    teacher_john.print_self()
    teacher_jane.print_self()
#----------------------------------------------
# Sukuriame specializacijas
    specialization_programming = Specialization("Programming", 4.5)
    specialization_math = Specialization("Math", 4.0)
    specialization_english = Specialization("English", 3.5)

#----------------------------------------------
    program_computer_science.add_specialization(specialization_programming)
    program_computer_science.add_specialization(specialization_math)
    program_computer_science.add_specialization(specialization_english)

#----------------------------------------------
# paskirstome studentus i specializacijas
    program_computer_science.assign_students_to_specializations()

#----------------------------------------------
# isvedame specializacijas
    for specialization in program_computer_science.specializations:
        specialization.print_self()

    # Isvedame bendra vidurki
    print(f"\nTotal average grade: {calcTotalAverageGrade(program_computer_science):.2f}")

#----------------------------------------------
# Nuskaitome duomenis is failo
def load_students_from_file(filename):
    students = []
    with open(filename, "r") as file:
        data = json.load(file)
        for student_data in data:
            student = Student(
                student_data["firstname"],
                student_data["lastname"],
                student_data["age"],
                student_data["financingstatus"])
            for subject in student_data["subjects"]:
                grades = Grades(subject["grades"])
                subject = Subject(subject["name"], subject["credits"])
                student_subject_grades = StudentSubjectGrades(subject, grades)
                student.add_subject_grade(student_subject_grades)
            students.append(student)
    return students

# issaugome specialybes priskirtas studentus i faila
def save_specilizations_to_file(specializations,filename):
    data = [] 
    for specialization in specializations:
        specialization_data = {
            'name': specialization.name,
            'grace_threshold': specialization.grade_threshold,
            'students': [
                {
                    'firstname': student.firstname,
                    'lastname': student.lastname,
                    'average_grade': student.average_grade()
                }
                for student in specialization.students
            ]
        }
        data.append(specialization_data)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
#----------------------------------------------

def CreateRegexTest():
    students = [
    Student("John", "Doe",20,"self-financed"),
    Student("Jane", "Doe",21,"self-financed"),
    Student("Alice", "Smith",24,"self-financed"),
    Student("Bob", "Brown",23,"self-financed")
    ]

    students[0].add_subject_grade(StudentSubjectGrades(Subject("Programming", 5), Grades([4, 5, 3])))
    students[0].add_subject_grade(StudentSubjectGrades(Subject("Math", 4), Grades([3, 4, 5])))

    students[1].add_subject_grade(StudentSubjectGrades(Subject("History", 3), Grades([5, 5, 4])))
    students[1].add_subject_grade(StudentSubjectGrades(Subject("Programming", 5), Grades([4, 5, 4])))

    students[2].add_subject_grade(StudentSubjectGrades(Subject("Literature", 3), Grades([3, 2, 4])))
    students[2].add_subject_grade(StudentSubjectGrades(Subject("Math", 4), Grades([4, 5, 5])))

    students[3].add_subject_grade(StudentSubjectGrades(Subject("Programming", 5), Grades([4, 3, 5])))
    students[3].add_subject_grade(StudentSubjectGrades(Subject("Art", 2), Grades([5, 4, 4])))
    return students


def filterStudentsBySubject(students, subject_pattern):

    filtered_students = []
    for student in students:
       
        for subject_grade in student.subject_grades:  
            if re.search(subject_pattern, subject_grade.subject.name, re.IGNORECASE):
                filtered_students.append(student)
                break  
    return filtered_students

def RegexOperations():
    subject_name = "Programming"
    students=CreateRegexTest()
    filtered_students = filterStudentsBySubject(students, subject_name)
    print(f"Students that have subject {subject_name}:")
    for student in filtered_students:
        print(f"\nStudent: {student.firstname} {student.lastname}")
        for subject_grade in student.subject_grades:
                print(f"  Subject: {subject_grade.subject.name}")
             


# Failu operacijos 
def FileOperations():

    students = load_students_from_file("students.json")
    
    group_a = Group("A", 1)
    # priskiriame studentus grupei
    for student in students:
        group_a.add_student(student)

    specialization_math = Specialization("Math", 4.0)
    specialization_programming = Specialization("Programming", 4.5)
    # sukuriam programos objekta
    program = Program("Computer Science")
    program.add_group(group_a)
    program.add_specialization(specialization_math)
    program.add_specialization(specialization_programming)
    # priskiriame studentus i specialybes
    program.assign_students_to_specializations()
    # issaugojam specialybes i faila
    save_specilizations_to_file(program.specializations, "specializations.json")

createTest()
RegexOperations()
FileOperations()
