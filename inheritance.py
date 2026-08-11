# # Simple inheritance
# class Animal:
#     def __init__(self,name):
#         self.name = name
#         pass
#     def eat(self):
#         print(self.name, "is eating")

# class Dog(Animal):
#     def bark(self):
#         print(self.name, "is barking")

# d = Dog("Tomy")
# d.eat()
# d.bark()

# # Multiple inheritance
# class Father:
#     def __init__(self):
#         print("Father constructor.")

#     def skills(self):
#         print("Father: driving")

# class Mother:
#     def __init__(self):
#         print("Mother constructor")

#     def skills(self):
#         print("Mother: cooking")

# class Child(Mother,Father):
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)
#         print("Child constructor")

#     def studying(self):
#         print("Child: studying")

#     def hobbies(self):
#         print("Child: playing")

# c = Child()
# c.skills()
# c.hobbies()
# c.studying()

# Multilevel inheritance
# class Grandparent:
#     def __init__(self):
#         print("Grandparent constructor.")

#     def house(self):
#         print("Grandparent has a house")

# class Parent(Grandparent):
#     def __init__(self):
#         super().__init__()
#         print("Parent constructor.")

#     def car(self):
#         print("Parent has a car.")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor.")

#     def bike(self):
#         print("Child has a bike.")

# c = Child()
# c.house()
# c.car()
# c.bike()

# #Heirarchical inheritance 
# class Animal:
#     def __init__(self, name):
#         self.name= name
#         print("Animal constructor.")
#         pass

#     def eat(self):
#         print(self.name, "is eating.")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print("Dog constructor.")

#     def bark(self):
#         print(self.name, "is barking.")

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print("Cat constructor.")

#     def meow(self):
#         print(self.name, "is meowing.")

# d = Dog("Tomy")
# d.eat()
# d.bark()
# print()
# c = Cat("Forklift")
# c.eat()
# c.meow()

# #Hybrid inheritance
# class Animal:
#     def __init__(self):
#         print("Animal constructor.")

#     def eat(self):
#         print("Animal is eating.")

# class Dog(Animal):
#     def dog_sound(self):
#         print("Dog says woof.")

# class Cat(Animal):
#     def cat_sound(self):
#         print("Cat says meow.")

# class Pet(Dog,Cat):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Pet constructor.")

#     def play(self):
#         print("Pet is playing.")

# p = Pet()
# p.eat()
# p.dog_sound()
# p.cat_sound()
# p.play()

# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#         print("Person constructor")
#     def details(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)

# class Student(Person):
#     def branch(self):
#         print("Branch: Computer science")

# s = Student("Robert",20)
# s.details()
# s.branch()

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def emp(self):
#         print(f"Name: {self.name}\nSalary: {self.salary}")

# class Manager(Employee):
#     def branch(self):
#         print("Department: Aluva")

# e = Manager("Nikhil",45000)
# e.emp()
# e.branch()

class Person():
    def __init__(self,name):
        self.name = name

    def per(self):
        print("Name: ", self.name)

class Employee(Person):
    def __init__(self, name,employee_id):
        super().__init__(name)
        self.employee_id=employee_id
    def emp(self):
        print("Employee ID:", self.employee_id)

class Manager(Employee):
    def __init__(self, name, employee_id,department):
        super().__init__(name, employee_id)
        self.department = department

    def man(self):
        print("Department:",self.department)

m=Manager("Ashwin", 65000, "HR")
m.per()
m.emp()
m.man()