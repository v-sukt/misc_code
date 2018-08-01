#!/usr/bin/env python2.7
""" OOP is-a has-a relationships in comments """
# Animals is-a object (yes, sort of confusing) - inherits the object class
class Animal(object):
    
    def jump(self, n_times):
        for i in range(int(n_times)):
            print "Jumped For %s time" % i

# Dog is-an Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name (attribute)
        self.name = name
    
    def bark(self, noise):
        print "%s\n" % noise

# Cat is-an Animal
class Cat(Animal):
    
    def __init__(self, name):
        #Cat has-a name (Attribute)
        self.name = name
    
    def miyao(self):
        print "Doing Miyaoo" 
    

# Person is an object - inherits the object class
class Person(object):
    
    def __init__(self, name):
        # Person has-a name
        self.name = name
        
        # Person has-a pet of some kind
        self.pet = None

# Employee is a Person
class Employee(Person):
    """ Inherits the Person class, there can be muiltiple inheritance - but it has some issues with multiple __init__() methods being called from child of these classes """
    
    def __init__(self, name, salary):
        # Set the name Employee who is-a Person (so inherits the name attribute)
        super(Employee, self).__init__(name) 
        
        """ super(type [,type-or-object])
        so this says super of Employee for self object(current instance).__init__() method
        There are issubclass(Employee, Person) isinstance() functions that can be used to check 
        object provides mro() method - ??? """
        
        # Employee has-a salary
        self.salary = salary

# Fish is an object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")
rover.bark("wow - wow")

# satan is-a Cat
satan = Cat("Satan")
satan.jump(3)

# mary is-a Person - instance of class Mary which has-a name "Mary"
mary = Person("Mary")

# mary's pet is set to satan (mary object's pert attribute set to Cat object named satan)
mary.pet = satan

# Frank is an employee with name = Frank and salary 120000
frank = Employee("Frank", 120000)

# frank who is-a employee person who has-a pet that is set to Dog named Rover
frank.pet = rover

# flipper is a Fish
flipper = Fish()

# crouse is Salmon Fish
crouse = Salmon()

# harry si Halibut Fish
harry = Halibut()
