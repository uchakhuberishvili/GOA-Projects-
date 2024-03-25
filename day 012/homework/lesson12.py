#1

budget = int(input("enter your budget: "))
chocolate_chips = 10
if budget >= chocolate_chips:
    print("u can afford chocolate chips")
else:
    print("you can't afford chocolate chips")

#2

i = password = ("GoaBest123")
user_input = 0
while user_input != password:
    user_input = input("enter the password: ")
    print("incorrect")
    print("this is your", i ,"th try")
    i += 1
    if i == 5:
        print("your are blocked")
if user_input == password:
    print("correct")

#3

user_input1 = int(input("enter our min number: "))
user_input2 = int(input("enter your max number: "))
user_step = int(input("enter your steps: "))
for i in range(user_input1,user_input2,user_step):
    print(i)

#4

s1 = input("Please Enter Side  1 ")
s2 = input("Please Enter Side  2 ")
s3 = input("Please Enter Side  3 ")
overall = (s1+s2>s3) and (s1 + s3 > s2) and (s2 +s3 > s1)
while overall != True:
     s1 = input("Please Enter Side  1 ")
     s2 = input("Please Enter Side  2 ")
     s3 = input("Please Enter Side  3 ")
     overall = s1+s2>s3

#5

operation = input("pplease enter operation (+,-,/,*); ")
num1 = int(input("pleas enter first number: "))
num2 = int(input("pease enter second number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)

else:
    print("operation  in not valid")
