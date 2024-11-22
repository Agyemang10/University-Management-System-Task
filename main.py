class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
    def get_student_summary(self):
        return f"{self.get_details()}\nStudent ID: {self.student_id}, Course: {self.course}, Average Grade: {self.calculate_average_grade()}"
class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")
    def increase_salary(self, percentage):
        self.salary *= (1 + percentage / 100)
    def get_professor_summary(self):
        return f"{self.get_details()}\nStaff ID: {self.staff_id}, Department: {self.department}, Salary: {self.salary}"
class Administrator(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    def increment_service_years(self):
        self.years_of_service += 1
    def get_admin_summary(self):
        return f"{self.get_details()}\nAdmin ID: {self.admin_id}, Office: {self.office}, Years of Service: {self.years_of_service}"

student1 = Student("Alice Johnson", 20, "Female", "S1234", "Computer Science")
student2 = Student("Bob Smith", 21, "Male", "S5678", "Mathematics")
professor1 = Professor("Dr. Jane Doe", 45, "Female", "P1234", "Computer Science", 60000)
professor2 = Professor("Dr. John Smith", 50, "Male", "P5678", "Mathematics", 70000)
admin = Administrator("Mary Brown", 35, "Female", "A4321", "Room 10, Admin Block", 5)
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(75)
professor1.give_feedback(student1, "Excellent work, keep it up!")
professor2.increase_salary(10)
admin.increment_service_years()
