'''
Module to can show all data from students, teachers and the schcool 
Using diferent classes  one to show literaly one to the students and one to the teachers
'''

#Class to take the principal data and show it


class User():
    
    def __init__(self, name, age, code):
        self.name = name
        self.age = age
        self.code = code

    def show_data(self):
        print(f'Name:{self.name}\nAge:{self.age}\nCode:{self.code}')

'''
Class which catch and show the teacher data
That inherits the functions of the class User
'''
class Professor(User):
    #functions to catch the data
    def __init__(self, name, age, code, courses, project, salary, budget):
        super().__init__(self, name, age, code)#line which instance the functions of the super class
        self.courses = courses
        self.project = project
        self.salary = salary
        self.budget = budget
    
    #Show the data
    def prof_data(self):
        print(f'User type: Teacher \n Data:\n{User.show_data()}')
        print(f'Courses:{self.courses}\nSalary:{self.salary}\nProjects:{self.project}')
    
    #Show and control the budrget for every project
    def prof_budget(self):
        print(f'Name{self.name}budget{self.budget}')

'''
Class which catch and show the students data
That inherits the functions of the class User
'''    
class Student(User):
    def __init__(self, name, age, code, course, debt):
        super().__init__(self, name, age, code)#line which instance the functions of the super class
        self.course = course    
        self.debt = debt
    #Show the data
    def student_data(self):
        print(f'User type: Student \n Data:\n{User.show_data()}\nCourse:{self.course}\n=Debt:{self.debt}')
    
    #show and control the debt of the student
    def student_debt(self):
        print(f'Name{self.name}\nDebt{self.debt}')

'''
Class which catch and show the school data
That inherits the functions of the class User
'''    
class School():
    def __init__(self, name, budget, students, teachers):
        self.name = name
        self.budget = budget
        self.students = students
        self.teachers = teachers
    
    def show_data(self):
        print(f'Name:{self.name}\nBudget:{self.budget}\nStudents Total:{self.students}\nTeachers Total:{self.teachers}')

college = School('Liceo Campestre Cafam',9999999999999999,['Juan Esteban Cortez Mendez','Esteben Ardila Gonzalez','Laura Stephanie Suarez Garcia'],['Juan Esteban Cortez Mendez','Esteben Ardila Gonzalez','Laura Stephanie Suarez Garcia'])      
college.show_data()            