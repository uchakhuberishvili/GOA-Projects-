#1

def multiply(a, b):
    print(a * b)
multiply(5,10)

#2

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(even_or_odd(14))
print(even_or_odd(123))

#3

userinput = input("enter a number: ")
def number_to_string(num):
    return str(num)

print(number_to_string(userinput))

#4

def solution(goa):
    return goa[::-1]
print(solution("hellouu"))

#5

def positive_sum(arr):
    overall = 0
    for num in arr:
        if num >= 0:
            overall += num
    return overall

print(positive_sum([20,-10,30,40]))

#my

def multiple(number,num):
    return number * num
print(multiple(20,10))

def divide(number,num):
    return number // num
print(divide(100,20))

def Sum(number,num):
    return number + num
print(Sum(12238689,12345534))