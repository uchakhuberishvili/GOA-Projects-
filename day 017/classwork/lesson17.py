name_lastname = input("please enter your name and lastname: ")
for i in range(0,len(name_lastname)):
        print(name_lastname[i])

name_lastname1 = input("please enter your name and lastname: ")
for i in range(0,len(name_lastname1),2):
        print(name_lastname1[i])

cart = ["apple","bananna","mango","orange"]
if "mango" in cart:
        print(True)