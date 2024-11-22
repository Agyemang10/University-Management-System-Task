class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Student(Person):
    def __init__(self):
        super().__init__()
        self.student_id = ""
        self.course = ""
        self.grades = []
        self.mentor = None  

    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    