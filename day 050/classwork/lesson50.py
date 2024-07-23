def make_negative(number):
    number = str(number)
    neg = "-" + number
    if "-" in number:
        return int(number)
    neg = int(neg)
    return neg
print(make_negative(20))

def validate_pin(pin):
    Leng = len(pin)
    if Leng == 4 or Leng == 6:
        return True
    else:
        return False
print(validate_pin("1234344"))