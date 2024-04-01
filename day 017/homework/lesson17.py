names = ["nika","luka","daviti","giorgi","sandro"]
print(names[0],names[1],names[2],names[3],names[4])
for i in names:
    print(i)
sum = 0
number = [1,2,3,4,5,6,7,8,9,10]
for i in number:
    sum = sum + i
    print(sum)
sums = 1
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    sums = sums * i
    print(sums)
numbs = [1,2,3,4,5,6,7,8,9,10]
sumss= 0
for i in numbs:
    if i %2 == 0:
        sumss = sumss + i
        print(sumss)
sumsss = 1
numberss = [1,2,3,4,5,6,7,8,9,10]
for i in numberss:
    if i %2 != 0:
        sumsss = sumsss * i
        print(sumsss)
best = "cristiano"
print(best[0],best[1],best[2],best[3],best[4],best[5],best[6],best[7],best[8])
name = "aleksandre"
even_string = ''
for i in range(0,len(name)):
    if i % 2 ==0:
        print(name[i])

