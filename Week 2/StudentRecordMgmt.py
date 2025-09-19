
class Student:
    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Department: {self.department}")
        print("-" * 30)

    def update_grade(self, new_grade):
        self.grade = new_grade

# Main section
if __name__ == "__main__":
    # Create student objects
    student1 = Student("SU", "A", "Computer Science")
    student2 = Student("QI", "B", "Mechanical Engineering")
    student3 = Student("SO", "C", "Electrical Engineering")

    # Print initial student information
    print("Initial Student Records:")
    student1.print_info()
    student2.print_info()
    student3.print_info()

    # Update grade of one student
    print("Updating Charlie's grade to B+...\n")
    student3.update_grade("B+")

    # Print updated information
    print("Updated Student Records:")
    student3.print_info()
