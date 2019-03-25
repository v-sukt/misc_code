

# Animal is-a object (yes, sort of confusing) look at the notes
class Animal(object):
    pass


# Dog is-an Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-an Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is an Object - Inherits the base class called object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        # Initialize the __init__() of the Parent of the Class
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-an object
class Fish(object):
    pass


# Salmnn is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog - it has-a name "Rover"
rover = Dog("Rover")

# satan is-a Cat - it has-a name Satan
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet satan which is-a Cat
mary.pet = satan

# frank is-a Employee which has-a Frank and has-a salary of 120000
frank = Employee("Frank", 120000)

# frank has-a pet rover which is-a Dog
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
