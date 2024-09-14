def calculator():
    first = int(input("enter your first number: "))
    second = int(input("enter your second number: "))
    task = input("enter * or // or + or - : ")
    if task == "*":
        return "the answer is " + str(first * second)
    elif task == "//":
        return "the answer is " + str(first // second)
    elif task == "+":
        return "the answer is " + str(first + second)
    elif task == "-":
        return "the answer is " + str(first - second)
    else:
        return "enter one of these four: *,//,+,-"
print(calculator())

def array(lists):
    result = 0
    for i in lists:
        result += i
    return result
print(array([12,32,53,43,23,11]))

def arithmetic_mean(numbers):
    if len(numbers) == 0:
        return "The list is empty"
    
    total = sum(numbers)
    mean = total / len(numbers)
    return mean


