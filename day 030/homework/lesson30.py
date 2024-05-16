def upper_rev(name):
    rev = name[::-1]
    upper = rev.upper()
    return upper
print(upper_rev("hello"))

def odd_even(names):
    odd = []
    even = []
    for i in names:
        if len(i) % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
    return [odd, even]

names = ["vano", "davit", "zuka", "yiyliyo"]
result = odd_even(names)
print(result[0])
print(result[1])


def upper_cap(names):
    odd = []
    even = []
    for name in names:
        if len(name) % 2 == 0:
            even.append(name.upper())
        else:
            odd.append(name.capitalize())
    return odd,even
print(upper_cap(["goa_best" , "vano" , "nesvi" , "tskhVarAdzE"]))



def islow_up(names):
    upper = []
    lower = []
    for i in names:
        if i.isupper():
            lower.append(i.lower())
        elif i.islower():
            upper.append(i.upper())
    return upper,lower
print(islow_up(["vano" , "DAVIT" , "LUKA" , "nika"]))


def find(Str):
    index = Str.find("n")
    if index % 2 == 0:
        return Str.upper()
    else:
        return Str.capitalize()

test_case = "vano motiashvili"
result = find(test_case)
print(result)