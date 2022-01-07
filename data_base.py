'''
This class its to mantain the data of the techers students and tne school                              
Using objectso with the data of each one
'''
from user_data import Professor, School, Student


class data ():

    ready = True
    def __init__(self, number):
        self.number = number
    
        if number == "thc":
            def teacher(self):
              
                Professor.prof_data('Juan Esteban Cortez Mendez',32,20201253001,['Mathematics1','Basic software development'],['Calculator','Basement sustain'],1300)
                Professor.prof_data('Esteben Ardila Gonzalez',23,20211253051,['Spanish3','Phisic education'],['play about Romeo and Julieth','Giant Diccionary'],1300)
                Professor.prof_data('Laura Stephanie Suarez Garcia',43,20191753987,['Dances','Plastic Arts'],['Band','Painting'],1300)   
                
        elif number == "std":
            def student(self):   
                
                Student.student_data('Juan Esteban Cortez Mendez',12,20201253001,['Mathematics1','Basic software development'],1300)
                Student.student_data('Esteben Ardila Gonzalez',13,20211253051,['Spanish3','Phisic education'],1300)
                Student.student_data('Laura Stephanie Suarez Garcia',15,20191753987,['Dances','Plastic Arts'],1300)
                
        elif number == "sch":
            School.show_data('Liceo Campestre Cafam',9999999999999999,['Juan Esteban Cortez Mendez','Esteben Ardila Gonzalez','Laura Stephanie Suarez Garcia'],['Juan Esteban Cortez Mendez','Esteben Ardila Gonzalez','Laura Stephanie Suarez Garcia'])      
        else:
            print("Tipo de usuario eqivocado")