numberss = []

start = 20
end = 5 + 3
step = -1

while start > end:
    numberss.append(start)
    start = start + step

print(numberss)

#1

user_input = input("enter a word: ")

len = len(user_input)
if len > 3:
    print(user_input[0:3])
elif len == 3:
    print(user_input[0])
elif len < 3:
    print(user_input[0])

#2

numbers = []

for i in range(10,21):
    if i % 2 ==0:
        numbers.append(i)
print(numbers)

#3

userinput = input("enter something: ")
reversed = userinput[::-1]
print(reversed)