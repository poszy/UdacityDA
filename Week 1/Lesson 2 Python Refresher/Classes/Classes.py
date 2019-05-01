#!/usr/bin/python

# self, which is used to reference a class instance's own variables and functions from within the class definition
# if we had a class called Person and we wanted the class instances to have a variable called age, we could store this information by using self.age

# a function that would increment the age of the person, we could define a function inside this class called def birthday(self).
# In order to be a class function, birthday needs to include the input variable self, this is proper referencing.

# the class initializer, def __init__(self), is where variables should be added, the variables are initizlzed hereself.
# SELF must be used when defclaring a variable in an ___init___ function so that each isntance of the class has its own copy of that variable


class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age = self.person_age + 1

    def getName(self):
        return self.person_name

#function for getting the classs variable. This is called an Accessor
bob = Person('Bob', 32)
print(bob.getName())

# Calling the birthday fucntion to change the age is called a mutator
bob.birthday()
print(bob.person_age)
