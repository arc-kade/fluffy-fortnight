class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        pass
    def display_details(self):
        print(f"Car brand = {self.brand}, Car model = {self.model}, Car year = {self.year}")

car1= Car("Toyota","Celica",1995)
car2 = Car("Nissan","Silvia",1993)
# car1.display_details()
# car2.display_details()
class Student:
    def __init__(self):
        print("First Constructor")
    def __init__(self):
        print("Second Constructor")
    def display(self,name):
        print(name)

s1= Student()             #Method overriding
s1.display("Jane Doe")