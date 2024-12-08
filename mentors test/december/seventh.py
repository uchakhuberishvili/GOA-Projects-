def prime(n):
    if n < 2: #თუ N ნაკლებია 2ზე მაშინ ის არ არის მარტივი რიცხვი
        return False
    for i in range(2, int(n**0.5)+ 1):#ვამოწმებთ 2 დან n ის კვადრატის ფესვამდე ყველა რიცხვით გაყოფას
        if n % i == 0:#თუ n იყოფა i-ზე უნაშთოდ,n არ არის მარტივი რიცხვი
            return False
    return True #თ ყველაფერი გაიარა, n არის მარტივი რიცხვი
def find(start,end):
    primes = [num for num in range(start,end + 1)if prime(num)]#ვქმნით სიას,სადაც ვამატებთ ყველა რიცხვს startდან end მდე,რომლებიც მარტივია
    return primes#ვაბრუნებთ სიას
print(find(10,20))
print(find(1,10))
print(find(20,30))
print(find(24,25))
print(find(1,1))