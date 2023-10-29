# Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog:
    def bark(self):
        print("Dog is barking")

class Cat:
    def meow(self):
        print("Cat is meowing")

d = Dog()
d.bark()

c = Cat()
c.meow()

