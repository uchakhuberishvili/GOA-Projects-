x = ['111','2222222222222', '22','2222']
integer = []
string = []
for i in x:
    integer.append(int(i))
integer = sorted(integer)
for i in integer:
    i = str(i)
    string.append(i)
print(string)

def validate_pin(pin):
    Leng = len(pin)
    if Leng == 4 or Leng == 6:
        return True
    else:
        return False
print(validate_pin("1234344"))

def opposite(number):
    neg = 0
    pos = 0
    if number > 0:
        neg -= number * 2
    if number <0:
        pos += number * 2
    return [neg,pos]
print(opposite(20))