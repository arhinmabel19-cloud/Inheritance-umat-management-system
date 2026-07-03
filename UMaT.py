class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

#child class:student
class Student(Person):
    def __init__(self,name,age,student_id):
          super().__init__(name,age)
          self.student_id = student_id

    def enroll_course(self,course):
        print(f"{self.name} is enrolled in {course}")

#overriding display_info()
    def display_info(self):
        super().display_info()
        print(f"Student ID:{self.student_id}")

#child class: Lecturer
class Lecturer(Person):
    def __init__(self,name,age,employee_id):
          super().__init__(name,age)
          self.employee_id = employee_id

    def teach_course(self,course):
        print(f"{self.name} is teaching {course}")

#creating objects
student1 = Student("Arhin Mabel Nyarko",20,"FOE4100604425")
lecturer1 = Lecturer("Dr. Matthew Cobbinah",38,"EM9005")

print("Student Information:")
student1.display_info()

print("n\Lecturer Information:")
lecturer1.display_info()

print()
student1.enroll_course("Object-Oriented Programming")
lecturer1.teach_course("Object Oriented Programming")