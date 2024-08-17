class Car:

    def turn_on(self):
        print("you start the engine!")
        return self

    def drive(self):
        print("you drive the car!")
        return self

    def brake(self):
        print("you step on the brakes!")
        return self
    
    def turn_off(self):
        print("you turn off the engine!")
        return self
    
car = Car()

car.turn_on().drive()

car.brake().turn_off()

car.turn_on().drive().brake().turn_off()


class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")
class Fish(Animal):
    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")
class Hawk(Animal):
    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.slumber()