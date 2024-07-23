#user input
user_input1 = int(input("enter your first number: "))
user_input2 = int(input("enter your second number: "))
user_input3 = int(input("enter your third number: "))
print(user_input1 + user_input2 + user_input3)
print(user_input1 - user_input2 - user_input3)
print(user_input1 * user_input2 * user_input3)
print(user_input1 + user_input2 - user_input3)
print(user_input1 * user_input2 // user_input3)
print(5 + 5)
print(int("5") + 20)
print(int(20 // 10))
print(type(10))
print(type("goabest"))
print(type(23.11))
print(23 * int("17"))
#if
money = 0
if money > 0:
    print("you can afford")
else:
    print("u can't afford")
boys = 3
girls = 7
print(girls > boys)
print(boys > girls)
#for loops
for i in range(0,21):
    print(i)
userinput = int(input("enter your number: "))
userinputagain = int(input("enter your number again: "))
for i in range(userinput,userinputagain):
    print(i)
for i in range(50,101):
    print(i)
for i in range(50,101,-1):
    print(i)
for i in range(0,51):
    print(i + i)
userinputer = int(input("enter a whole number: "))
for i in range(0,userinputer):
    print(i)
userinputage = int(input("enter your age: "))
thisyourage0yearslater = userinputage + 10
for i in range(userinputage,thisyourage0yearslater):
    print(i)
x = 777
y = 1233123233
z = -66564

print(type(x))
print(type(y))
print(type(z))
for i in range(0,51):
    print(i * 5)
for i in range(2,20):
    if i % 2 == 0:
        print(i)
for i in range(0,51,5):
    print(i)
for i in range(5,11):
    print(i * i)
user = int(input("enter a number: "))
final = 1
for i in range(1, user + 1):
    final *= i 
userinputbruh = int(input("enter a number: "))
if userinputbruh % 2:
    print(userinputbruh % 2)
else:
    print(userinputbruh * 3 + 1)
#if else/while loops
num = 0
while num != 10:
    print(num)
    num += 1
username = 0
while username != "quit":
    username = input("enter your name: ")
if username == "quit":
    print("access granted")
else:
    print("access denied")
numb = 10
while numb !=20:
    print(numb)
    numb += 1
#elif
usernum = -1
while usernum != 1:
    usernum = int(input("enter a number: "))
if usernum > 0:
    print("correct")
elif usernum == 0:
    print("wrong")
else:
    print("wrong")
number = 0
while number <11:
    print(number * number)
    number += 1
#keys
clubs = ["manunited","mancity","realmadrid"]
clubs.append("arsenal")
clubs.sort()
clubs.pop()
print(clubs)
#def function
def Goa(acc1,acc2):
    print(acc1 + " is the best academy")
    print("Not" + acc2)
Goa("Goa")
Goa("novatori")
def multiply(number1,number2):
    result = number1 * number2
    return result
print(multiply(6,8))
def gamarjoba(first,middle,last):
    gamarjoba(first="ucha",middle="dzlieri",last="kuberishvili")
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
print(round(abs (float(input("Enter a whole positive number: ")))))
name = ("bro")
def display():
    name="code"
    print(name)
print=(name)
def add(num1,num2):
    sum = num1 + num2
    return sum
#args
print(add(1,2))
def add(*args):
    sum = 0
    for i in args:
        sum += i
        return sum
print(add(1,2,3,4,5,6,7,8,9,10))
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
        return sum
#kwargs
print(add(1,2,3,4,5,6))
def hello(**kwargs):
    print("Hello" +kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
#format
hello(first="bro",middle="Dude",last="Code")
animal = "cow"
item = "moon"
print("The "+animal+"jumped over the"+item)
print("The {} jumped over the {}".format(animal,item))
print("The {0} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))
text = "The {} jumped over the {}"
print(text.format(animal,item))
name = "bro"
print("hello, my name is {}".format(name))
print("hello, my name is {:10}nice to meet you".format(name))
print("hello, my name is {:>10}nice to meet you".format(name))
print("hello, my name is {:<10}nice to meet you".format(name))
print("hello, my name is {:^10}nice to meet you".format(name))
number = 3.14159

print("The number pi is {:.2f}".format(number))
number = 1000
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:e}".format(number))
print("The number pi is {:E}".format(number))
#random
import random
o = random.randint(1,6)
p = random.random
mylist = ["rock","paper","scissors"]
z = random.choice(mylist)
cards = [1,2,3,4,5,6,7,8,9,10,"j","q","k","a"]
random.shuffle(cards)
print(cards)
print(o)
print(z)
print(p)
numerator = int(input("enter a number to divide: "))
denominator = int(input("enter a number to divide by: "))
result = numerator / denominator
print(result)
import os
#file
path = "C:\\Users\\admin\Desktop\\text.txt"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("tha location doesn't exist!")
with open("C:\\Users\\admin\\Desktop") as file:
    print(file.read())
print(file.closed)
#file create
text = "Yoooooooooooo\nThis is some text\nHave a good one!"
with open("C:\\Users\\admin\\Desktop","w") as file:
    file.write(text)
#file add
import shutil
shutil.copyfile("C:\\Users\\admin\\Desktop","copy.txt")
def hello():
    print("have a nice day!")
#rock paper scissors
import random
while True:
    choice = ["rock","paper","scissors"]
    player = None
    computer = random.choice(choice)
    while player not in choice:
        player = input("rock,paper.scissors?: ").lower()
    if player == computer:
       print("computer: ",computer)
       print("player: ",player)
       print("Tie")
    elif player == "rock":
       if computer == "paper":
           print("computer: ",computer)
           print("player: ",player)
           print("You lose!")
       if computer == "scissors":
               print("computer: ",computer)
               print("player: ",player)
               print("You Win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win!")
    elif player == "rock":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")
        if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose!")
    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
         break
print("Bye")

#quiz game

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)        
        question_num += 1
    display_score(correct_guesses,guesses)
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
def display_score(correct_guesses,guesses):
    print("--------")
    print("RESULTS")
    print("ANSWERS:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses:", end=" ")
    for i in guesses:
        print((i), end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score)+"%")



def play_again():
    
    response = input("Do you want to play again? (yes or no)")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
"Who created Python?: ": "A",
"What year was Python created?: ": "B",
"Python is tributed to which comedy group?: ": "C",
"Is the Earth round?: ": "A"}
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"], 
["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
new_game()
while play_again():
    new_game()

print("BYEEEEEEEEE!!!!!")

#OP

class Car:

    make = None
    model =None
    year = None
    color = None

    def __init__(self,make,model,year,color):
        self.make =make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("thisthis "+self.model+" is driving")
    def stop(self):
        print("this "+self.model+"  is not driving")


car_1 = Car("chevy","corvette",2021,"blue")
car_2 = Car("ford","mustang",2022,"red")
print(car_1.make)
    
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive
car_1.stop()
print(car_2.make)
    
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive
car_2.stop()

#class variables

from car import Car

car_1 = Car("chevy","corvette",2021,"blue")
car_2 = Car("ford","mustang",2022,"red")

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)

#inheritance

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

#method overriding

class Animal:

    def eat(self):
        print("This animal is eating!")

class Rabbit(Animal):
    
    def eat(self):
        print("This rabbit is eating a carrot!")


rabbit = Rabbit
rabbit.eat()

#method chaining


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

#super function!


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    
class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length , width)

class Cube(Rectangle):

    def __init__(self, length, width , height):
        super().__init__(length , width ,)
        self.height = height

    def volume(self):
        return self.length*self.height

square = Square(3 , 3)
cube = Cube(3 , 3)
print(square.area())
print(cube.volume())

#abstract class!

#abstract method!


from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("you drive the car!")
   
    def stop(self):
        print("this car is stopped!")

class Motorcycle(Vehicle):

    def go(self):
        print("you ride the motorcycle!")
    
    def stop(self):
        print("this motorcycle is stopped")

vehicle = Vehicle()

car = Car()

motorcycle = Motorcycle()

vehicle.go

car.go

motorcycle.go

#ojects as arguments

class Car:

    color = None

class Motorcycle:

    color = None


def change_color(car,color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")

change_color(car_2,"white")

change_color(car_3,"blue")

change_color(bike_1,"black")

print(car_1.color)

print(car_2.color)

print(car_3.color)

print(bike_1.color)



#duck typing!

class Duck:

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is qwuacking")

class Chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter!")

duck = Duck()

chicken = Chicken()

person = Person()

person.catch(chicken)

#walrus operaton :=

happy = True
print(happy)

print(happy = True)

foods = list()
while True:
    food = input("what food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

foods = list()

while food := input("what food do you like?: ") != "quit":
    foods.append(food)


def hello():
    print("Hello")

print(hello)

hi = hello

print(hi)

hi()

hello()

say = print

print()

say("Whoa! i can't believe this works! :O")

#higher Order Function! 1.


def loud(text):
    return text.upper()

def quiet(text):
    text.append("!!!")
    return text.lower()

def hello(func):
    text = func("Hello!")
    print(text)

hello(loud)
hello(quiet)

#Higher Order Function! 2.

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)

print(divide(10))


#lambda parameters:expression!


#def double(x):
#    return * 2

#print(double(5))

double = lambda x:x * 2

print(double(5))

multiply = lambda x , y : x * y

add = lambda x,y,z:x + y + z
#full_name = lambda first_name,last_name:first_name,+" "+ last_name
age_check = lambda age:True if age >= 18 else False
#print(full_name("bro","code"))
print(age_check(12))
print(add(5,6,7))

