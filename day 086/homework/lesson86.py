def even_odd():
    user_input = int(input("enter an integer: "))
    if user_input % 2 ==0:
        return "even"
    else:
        return "odd"
print(even_odd())


def time_travel():
    user_input1 = int(input("what year are you in?: "))
    current_year = user_input1
    user_input2 = int(input("how old are you?: "))
    current_age = user_input2
    print("you are in year " + str(current_year) + " and you are " + str(current_age) + " years old")
    travel_year = int(input("what year do you want to go in?: "))
    if travel_year < current_year:
        back = current_year - travel_year
        current_year = current_year - back
        current_age = current_age - back
    elif travel_year > current_year:
        forward = travel_year - current_year
        current_year = current_year + forward
        current_age = current_age + forward
    print("you are in year " + str(current_year) + " and you are " + str(current_age) + " years old")
time_travel()

def add_one():
    user_input = int(input("enter a number: "))
    return user_input + 1

def cool():
    user_input = int(input("enter a number: "))
    if user_input > 10:
        return "მაგარია!"
    else:
        return user_input

def lowest():
    user_input1 = int(input("enter first number: "))
    user_input2 = int(input("enter second number: "))
    if user_input1 > user_input2:
        return user_input2
    else:
        return user_input1
    
def length():
    user_input1 = str(input("enter a text: "))
    return len(user_input1)
print(length())

def sums():
    user_input1 = int(input("enter first number: "))
    user_input2 = int(input("enter second number: "))
    return user_input1 + user_input2

def number():
    user_input = int(input("enter a number: "))
    if user_input > 0:
        return "დადებითი"
    elif user_input < 0:
        return "უარყოფითი"
    elif user_input ==0:
        return "ნეიტრალი"
    
def boolean():
    user_input = int(input("enter a number: "))
    if user_input % 2 ==0:
        return True
    else:
        return False
    
def sums_5():
    user_input1 = int(input("enter first number: "))
    user_input2 = int(input("enter second number: "))
    return user_input1 + user_input2 + 5


