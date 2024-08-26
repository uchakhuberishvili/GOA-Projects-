name_lastname = input("please enter your name and lastname:")
for i in range(0,len(name_lastname)):
        print(name_lastname[i])

name_lastname1 = input("please enter your name and lastname:")
for i in range(0,len(name_lastname1),2):
        print(name_lastname1[i])


numbers = [1,2,3,4,5,6,7,8,9,20]
if 5 in numbers:
        print("yes")
else:
        print("no")

cart = ["apple","bnanna","mango","orange"]
if "mango" in cart:
        print(True)   

numbers = [1,2,3,4,5,6,7,8,9,10]

result = 0

for num in numbers:
    if num % 2 == 0:
        result = result + num

print(result)