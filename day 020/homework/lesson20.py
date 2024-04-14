user_input = input("enter a word that is same in reverse: ")
reversed = ''.join(reversed(user_input))

if user_input == reversed:
    print("word is palendrome")
else:
    print("word is not palendrome")

user_input = input("enter a word thats same in reverse: ")
reversed_word = " "
for i in range(len(user_input)-1,-1,-1):
    reversed_word += user_input[i]
    print(user_input[i])

if user_input == reversed_word:
    print(user_input, "is palidrome")
else:
    print(user_input,"is not palidrome")


repeatvalue = []
numbers = []
for i in range(5):
    num = int(input("please enter a number: "))
    numbers.append(num)

for n in numbers:
    count = numbers.count(n)
    if count > 1 and n not in numbers:
        print(n,"value count is", count)
        repeatvalue.append(n)

print(repeatvalue)
words_list = []

for i in range(5):
    word = input("Please enter word: ")
    words_list.append(word)

result = ""

for word in words_list:
    result += word[0]

print(result)