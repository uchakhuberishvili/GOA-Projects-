#hoo
def square_digits(num):
    string = ""
    for i in str(num):
        i = int(i)
        square = i * i
        string += str(square)
    return int(string)

def even_or_odd(number):
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"
    
