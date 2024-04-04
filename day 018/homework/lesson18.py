name = "Giorgi"
even_indexes_string = ''

for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

name = "aleksandre"
even_indexes_string = ''

for i in range(0, len(name)):
    if i % 2 != 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)

country = "georgia"
even_i_str = ''
for i in range(0,len(country)):
    if i % 2 == 0:
        even_i_str = even_i_str + country[i]
print(even_i_str)

country = "venezuela"
even_i_str = ''
for i in range(0,len(country)):
    if i % 2 != 0:
        even_i_str = even_i_str + country[i]
print(even_i_str)

academy = "goalorientedacademy"
evenistr = ''
for i in range(0,len(academy)):
    if i % 2 == 0:
        evenistr = evenistr + academy[i]
print(evenistr)

academy = "goalorientedacademy"
evenistr = ''
for i in range(0,len(academy)):
    if i % 2 != 0:
        evenistr = evenistr + academy[i]
print(evenistr)


num = 5

num = num + 6
num += 6

num = num - 1
num -= 1

num = num * 2
num *= 2

num = num / 2
num /= 2

num = num % 6
num %= 2

print(num)