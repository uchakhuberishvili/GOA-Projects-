def xbonacci(x,n):
    text = [1] * x#ვქმნით საწყისს მასივს,სადაც x ელემენტია 1
    if n <= x:#თუ n <= x,ვაბრუნებთ მხოლოდ პირველ n ელემენტს
        return text[:n]
    while len(text) < n:#ვავსებთ მასივს სანამ არ მივიღბთ n ელემენტს
        nextn = sum(text[-x:])#ბოლო x ელემენტების ჯამი
        text.append(nextn)
    return text
print(xbonacci(3,10))
print(xbonacci(2,10))
print(xbonacci(4,6))
print(xbonacci(5,8))
print(xbonacci(3,1))