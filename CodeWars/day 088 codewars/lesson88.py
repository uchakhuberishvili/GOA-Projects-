#6 kyu
def create_phone_number(n):
    phone = "("
    phone += str(n[0])
    phone += str(n[1])
    phone += str(n[2])
    phone += ")"
    phone += " "
    phone += str(n[3])
    phone += str(n[4])
    phone += str(n[5])
    phone += "-"
    phone += str(n[6])
    phone += str(n[7])
    phone += str(n[8])
    phone += str(n[9])
    return phone
#6 kyu

def up_array(arr):
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    num_str = ''.join(map(str, arr))
    num = int(num_str) + 1
    result = list(map(int, str(num)))
    return [0] * (len(arr) - len(result)) + result

#7 kyu


def odd_one(arr):
    for i, num in enumerate(arr):
        if num % 2 != 0:
            return i
    return -1

#7 kyu

def password(st):
    if len(st) < 8:
        return False
    if not any(char.isupper() for char in st):
        return False
    if not any(char.islower() for char in st):
        return False
    if not any(char.isdigit() for char in st):
        return False
    if not any(char in "!@#$%^&*()-_=+[{]};:,.<>/?" for char in st):
        return False
    return True

#7 kyu

def in_asc_order(arr):
    if sorted(arr) == arr:
        return True
    else:
        return False
    
#7 kyu

def longest(a1, a2):
    unique_chars = set(a1 + a2)
    sorted_chars = sorted(unique_chars)
    return ''.join(sorted_chars)
