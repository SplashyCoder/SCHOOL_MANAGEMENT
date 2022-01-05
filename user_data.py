from _typeshed import Self


class User():
    def __init__(self, name, age, code):
        self.name = name
        self.age = age
        self.code = code
    
    def show_data(self)
        print(f'Name:{self.name}\nAge: {self.age}\nCode:{self.code}')

class Professor(User):
    def __init__(self, name, age, code, courses, project, salary):
        super().__init__(self, name, age, code)
        self.courses = courses
        self.project = project
        self.salary = salary

    def prof_data(self):
        print(f'User type: Teacher \n Data:\n{User.show_data}\nCourses:{self.courses}\nProjects:{self.project}\nSalary:{self.salary}')
    
class Student(User):
    def __init__(self, name, age, code, course, debt):
        super().__init__(self, name, age, code)
        self.course = course
        self.debt = debt
    
    def student_data(self):
        print(f'User type: Student \n Data:\n{User.show_data}\nCourse:{self.course}\n=Debt:{self.debt}')
        
    

     
