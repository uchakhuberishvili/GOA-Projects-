def print_array(arr):
    result = ""
    for i in arr:
        result += str(i)
        result += ","
    result = result[:-1]
    return result
print(print_array(['a', 'b']))

def print_array(arr):
    return ",".join(map(str, arr))

print(print_array(['a', 'b']))


def operation(a, b):
    if a == b:
        return 0
    elif a % 2 == 0 and b % 2 == 1:
        return 1 + operation(a // 2, b)
    elif a % 2 == 1 and b % 2 == 0:
        return 1 + operation(a // 2, b)
    else:
        return 1 + operation(a // 2, b // 2)
    
def greet(language):
    lenguages = [ ("english", "Welcome")
, ("czech", "Vitejte")
, ("danish", "Velkomst")
, ("dutch", "Welkom")
, ("estonian", "Tere tulemast")
, ("finnish", "Tervetuloa")
, ("flemish", "Welgekomen")
, ("french", "Bienvenue")
, ("german", "Willkommen")
, ("irish", "Failte")
, ("italian", "Benvenuto")
, ("latvian", "Gaidits")
, ("lithuanian", "Laukiamas")
, ("polish", "Witamy")
, ("spanish", "Bienvenido")
, ("swedish", "Valkommen")
, ("welsh", "Croeso")
]
    for lang, greet in lenguages:
        if lang == language:
            return greet
    return "Welcome"