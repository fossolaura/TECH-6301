#Requirements

#Create a simple student database system that stores information about students, 
#such as their names, ages, and grades. Use classes to represent students and include 
#methods for displaying student information and calculating average grades.

class Student:
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()

    def print_scenario(self):
        print("Student Database System Scenario")
        print("--------------------------------")
        self.display_all_students()
        print("Average Grades of Students:")
        for student in self.students:
            print(f"{student.name}: {student.calculate_average():.2f}")

def main():
    # Create the student database
    db = StudentDatabase()

    # Adding new students to the database
    db.add_student(Student("Barbie", 20, [88, 92, 76, 81, 90]))
    db.add_student(Student("Ken Doll", 22, [95, 80, 84, 78, 85]))

    # Print a simple scenario of interactions
    db.print_scenario()

if __name__ == "__main__":
    main()
