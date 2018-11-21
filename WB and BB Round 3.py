#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:12:46 2018

@author: monicaalvarenga
"""
#%%

class IterGroup(type):
    def __iter__(cls):
        return iter(cls.allgroup)
    


class Student(metaclass=IterGroup):
    
    allgroup=[]
    
    def __init__(self, name, last_name, age, master):
        self.allgroup.append(self)
        
        self.name=name
        self.last_name=last_name
        self.age=age
        self.master=master
       
 
if __name__=='__main__':
       
    Alejandro=Student("Alejandro","Meneses",27,"MCSBT")
    Agata=Student("Agata","Kaczmarek",31,"MDBI")
    Anastasia=Student("Anastasia", "Lasunina",25,"MDBI")
    Aniken=Student("Anikken","Barstad",27,"MDBI")
    Candela=Student("Candela","Noya",24,"MDBI")
    Daniil=Student("Daniil", "Osipov",21,"MDBI")
    David=Student("David","Barrero Gonzalez",31,"MCSBT")
    Edem=Student("Edem","Francois",28,"MCSBT")
    Eduardo=Student("Eduardo","Paraja",23,"MDBI")
    Florian=Student("Florian","Diegruber",25,"MCSBT")
    Hannah=Student("Hannah","Oldorf",23,"MCBT")
    Isabella=Student("Isabella", "Rosenthal",27,"MDBI")
    Javier=Student("Javier", "Fernandez",24, "MCSBT")
    Lukas=Student("Lukas", "Hauser",28,"MDBI")
    Leila=Student("Leila", "Tazi",27, "MCSBT")
    Laura=Student("Laura", "Kageneck",23, "MCSBT")
    Monica=Student("Monica", "Alvarenga",28,"MDBI")
    Natalie=Student("Natalie", "Cedeno",26,"MDBI")
    Octavio=Student("Octavio", "Ramírez",28, "MDBI")
    Tancredi=Student("Tancredi", "Bernard",21, "MCSBT")
    Yasmine=Student("Yasmine", "Lyagoubi",23,"MDBI")
    Arthur=Student("Arthur", "Maroquene-Froissart",23, "MCSBT")

    for student in Student:
        print(student.name +" "+ student.last_name +" is a "+str(student.age)+" years old student from the "+student.master+
              " masters program")
    