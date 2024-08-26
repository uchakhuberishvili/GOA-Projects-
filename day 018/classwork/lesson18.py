names = ["me", "shen", "is", "chven", "tqven","isini"]

for i in names:
    print(i)

numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i %2 == 0:
        print(i)

numbers = [1,2,3,4,5,6,7,8,9,10]

odd_sum = 0
odd_multiple = 1

for num in numbers:
    if num % 2 != 0:
        odd_sum = odd_sum + num
        odd_multiple = odd_multiple * num

print("Odd numbers sum ", odd_sum)
print("Odd numbers multiple ", odd_multiple)
name = "Luka"

for char in name:
    print(char)
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
numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0
multiple = 1

for num in numbers:
    sum = sum + num
    multiple = multiple * num

print(numbers,"sum of these numbers is",sum)
print(numbers, "multiple of these numbers is", multiple)