class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInfo(self):
        print(f"Name: {self.name}, Email: {self.email}")

    @staticmethod
    def compareUsers(user1, user2):
        if user1.email == user2.email:
            return "Emails are the same."
        else:
            return "Emails are different."


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
       return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative!")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, studentID):
        super().__init__(name, age)
        self.studentID = studentID


student1 = Student("John", 20, "S12345")
print(f"Name: {student1.name}, Age: {student1.age}, Student ID: {student1.studentID}")
