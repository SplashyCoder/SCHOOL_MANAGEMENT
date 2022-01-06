'''
This class its to mantain the data of the techers students and tne school                              
Using two nested dictonares with the data of each one
'''
class data ():

    ready = True
    def __init__(self, number, typeof):
        self.number = number
        self.typeof = typeof
    
    if __init__.typeof == "thc":
            def teacher(self):
                teachers =[
                    {'number':1,'name':'Juan Esteban Cortez Mendez','Age':32,'code':20201253001,'courses':['Mathematics1','Basic software development'],'projects':['Calculator','Basement sustain'],'salary':1300},
                    {'number':2,'name':'Esteben Ardila Gonzalez','Age':23,'code':20211253051,'courses':['Spanish3','Phisic education'],'projects':['play about Romeo and Julieth','Giant Diccionary'],'salary':1300}
                    {'number':3,'name':'Laura Stephanie Suarez Garcia','Age':43,'code':20191753987,'courses':['Dances','Plastic Arts'],'projects':['Band','Painting'],'salary':1300}
                ]
        elif __init__.typeof == "std":
            def student(self):   
                students = [
                    {'number':1,'name':'Juan Esteban Cortez Mendez','Age':12,'code':20201253001,'courses':['Mathematics1','Basic software development'],'projects':['Calculator','Basement sustain'],'salary':1300},
                    
                ]

        else:
            print("Tipo de usuario eqivocado")