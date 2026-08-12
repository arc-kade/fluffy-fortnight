# # Public
# class Student:
#     def __init__(self):
#         self.name="Abilash"

# student = Student()
# print(student.name)

# # Private
# class BankAccount:
#     def __init__(self):
#         self.__balance = 5000
#         print(self.__balance)
# account = BankAccount()

# print(account.__balance)

# # Protected
# class Student:
#     def __init__(self,name):
#         self._name=name

# student=Student("Abilash")
# print(student._name)

# Example
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)
print("Balance: ", account.get_balance())