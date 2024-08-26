usernum = int(input("enter a number: "))
if usernum > 0:
    print("number is positive ")
elif usernum < 0:
    print("number is negative ")
else:
    print("number is 0")



userage = int(input("enter your age: "))
if userage >= 0 and userage<18:
    print("you are a child")
elif userage >= 18 and userage <50:
    print("you are a adult")
else:
    print("you are old")

