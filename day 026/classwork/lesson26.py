#print("ucha")

#for i in range(10):
#    print(" ucha ")

def name():
    for i in range(10):
        print("ucha")
name()

def nname(name):
    for i in range(10):
        print(name)

nname("uchas")

def nnname(name,amount):
    for i in range(amount):
        print(name)

nnname("ucha",5)



def quiz(start,end):
    for i in range(start,end):
        print(i)

quiz(10,20)


def quizz(start,end):
    overall = 0
    for n in range(start,end):
        overall += n
    return overall

print(quizz(1,5))



def quizzz(start,end):
    ovr = []
    for i in range(start,end):
        ovr.append(i)
    return ovr
start = 10
end = 30
result = quizzz(start,end)
print(result)

def name(name,index):
    print(name[index])
name("ucha",3)


def age():
    
    age = 0
    for i in range(100):
        age += 1
        print("you are now", age ,"old")
        if age == 18:
            
            print("you are now adult")
        
        if age == 60:
        
            print("you are now on pensia")
        if age == 100:
        
            print("YOU ARE VERY OLD")
        
age()


def calculate_sum(start, end):
    result = 0
    for i in range(start, end):
        result = result + i
    print(result)


calculate_sum(2,5)

def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)

def print_char(name, index):
    print(name[index])

print_char("Luka", 3)

def numbs(one,two):
    sums = one + two
    return sums
overall = numbs(12,28)
print(overall)

def even(name):
    return sum(name)
print(even([1,2,3,4,5]))
var1 = even([1,2,3,4,5])

def boom(shaka):
    total = 0

    for i in shaka:
        total += i
    return total
var2 = boom([1,2,3,4,5])
print(var2)