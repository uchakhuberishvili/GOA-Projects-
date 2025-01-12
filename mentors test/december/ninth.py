def primorial(n):
    result = 1#შედეგისთვის ვიწყებთ 1-ით
    for i in range(2,n+1): #გადავხედავთ რიცხვებს 2 დან n მდე
        if all(i % j != 0 for j in range(2,int(i**0.5)+1)):
            result *= i#თუ i მარტივია ვაბრუნებთ შედეგში
    return result
print(primorial(5))
print(primorial(10))
print(primorial(1))
print(primorial(7))
print(primorial(11))