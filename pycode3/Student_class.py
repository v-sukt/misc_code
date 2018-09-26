#!/usr/bin/env python3

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def disp(self):
        return("Name"+self.name+"age :"+str(self.age)+"Grade "+self.grade)

balram=Student("Balram",10,"5th")
krishna=Student("krishna",10,"5th")

