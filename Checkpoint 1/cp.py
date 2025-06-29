class Student:
    def __init__(self, name: str, grades: list = []):
        self.name = name
        self.grades = grades
        
    def add_grade(self, new_grade):
        self.grades.append(new_grade)
        
    def calculate_average(self):
        total = 0
        for i in self.grades:
            total+=i
        return total/(len(self.grades))
    
class GradeManager:
    def __init__(self, students: dict):
        self.students = students
        
    def add_student(self, name):
        self.students[name] = Student(name)
        
    def record_grade(self, name, grade):
        self.students[name].add_grade(grade)
    
    def calculate_average_all(self):
        for name, student in self.students.items():
            avg = student.calculate_average()
            print(f"{name}'s average grade: {avg}")
            
    def save_data(self, filename):
        with open(filename, 'w') as file:
            for name, student in self.students.items():
                avg = student.calculate_average()
                grades_str = ', '.join(map(str, student.grades))
                file.write(f"Name: {name}\n")
                file.write(f"Grades: {grades_str}\n")
                file.write(f"Average: {avg}\n")
                file.write("\n")

students_list = {
    "Alice": Student("Alice", [95, 87]),
    "Bob": Student("Bob", [78, 85, 92]),
    "Charlie": Student("Charlie", [60]),
    "Diana": Student("Diana", [100, 90, 95, 98]),
    "Ethan": Student("Ethan", [72, 65])
}
manager = GradeManager(students_list)
print("1. Add a new student | 2. Record a grade for a student | 3. Calculate the average grade of all students | 4. Save the data to a file | 5. Exit")
                
def navigator():
    choice = 0
    while choice!=5:
        choice = int(input("Enter your choice (1-5):"))
        if choice == 1:
            name = input("Enter the student's name: ")
            manager.add_student(name)
        elif choice == 2:
            new_grade = int(input("Enter the grade: "))
            name = input("Enter the student's name: ")
            manager.record_grade(name, new_grade)
        elif choice == 3:
            manager.calculate_average_all()
        elif choice == 4:
            file_name = input("Enter a file name: ")
            manager.save_data(f'{file_name}.txt')
        else:
            break
        
navigator()