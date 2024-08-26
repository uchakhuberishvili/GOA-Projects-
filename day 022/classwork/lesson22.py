list1 = "GoaTop"
print(list1[3:7])

list2 = ["banana","manana","apple","grape","orange","carrot"]
print(list2[0:4])

list33 = []
list3 = ["banana","manana","apple","grape","orange","carrot","lemon","mandarin"]

print(list3[::2])
#ან

for i in range(len(list3)):
    if i % 2 == 0:
        list33.append(list3[i])

print(list33)

numbers = []

start = 0

end = 10 + 1

step = 2

while start < end:
    numbers.append(start)
    start = start + step
print(numbers)


numbers = []

start = 0
end = 5 + 1
step = 1

while start < end:
    numbers.append(start)
    start = start + step

print(numbers)


names = ["Luka", "haroldi", "Nika", "dato", "gena"]

sliced_list = []

start = 0
end = 5
step = 2

while start < end:
    sliced_list.append(names[2])
    start = start + step

print(sliced_list)


numbers = []

start = 0
end = 5 + 1
step = 1

while start < end:
    numbers.append(start)
    start = start + step

print(numbers)