
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

print(is_isogram('Dermatoglyphics'))



def is_isogram_v2(string):
    string = string.lower()
    return len(string) == len(set(string))

print(is_isogram_v2('Dermatoglyphics'))



def is_isogram_v3(string):
    string = string.lower()
    return len(string) == len(set(string))

print(is_isogram_v3('Dermatoglyphics'))