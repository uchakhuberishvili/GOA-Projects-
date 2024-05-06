def numbers():
    numbs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    even = []
    for i in numbs:
        if i % 2 ==0:
            even.append(i)
    return even
print(numbers())


userinput = input("enter a number: ")

userinput = int(userinput)

def oddoreven(number):
    if number % 2 ==0:
        print("this number is even!")
    elif number % 2 !=0:
        print("this number is odd!")

print(oddoreven(userinput))

def nameslist():
    names = ["luka","nika","giorgi","ucha","saba","sandro"]
    capitalizenames = [first.capitalize() for first in names]
    return capitalizenames

print(nameslist())

def numberss():
    llist = [1,2,3,4,5,6,7,8,9,10]
    first_list = []
    second_list = []
    for i in llist:
        if i % 2 ==0:
            i // 2
            first_list.append(i)
        if i % 2 !=0:
            i * 2
            second_list.append(i)
    print(first_list,second_list)
print(numberss())