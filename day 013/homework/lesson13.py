#1

for i in range(1,51):
    if i % 3 == 0:
        print("fizz")    
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 and i % 5 == 0:
        print("fizzbuzz")
    else:
        print(i)


#2

user_input = int(input("please enter a number: "))
if user_input > 0:
    print("your number is positive")
elif user_input < 0:
    print("your number is negative")
else:
    print("your number is 0")

#3

for i in range(0,100,2):
    print(i)

#ან
    
for i in range(0,100):
    if i % 2 ==0:
        print(i)
#4

num1 = 0
num2 = 1
while (num2 <= 100):
  num1 += num2
  num2 += 1
  print(num1)

#5

week = int(input("enter number between 1 - 7: "))
if week == 1:
    print("thats sunday")
elif week == 2:
    print("thats monday")
elif week == 3:
    print("thats tuesday")
elif week == 4:
    print("thats wednesday")
elif week == 5:
    print("thats thursday")
elif week == 6:
    print("friday")
elif week == 7:
    print("saturday")
else:
    print("Bro Can't See")

#6
    
user_input = int(input("please enter a number: "))
if user_input % 2 ==0:
    print("number is even")
elif user_input == 0:
    print("number is 0")
else:
    print("number is odd")

