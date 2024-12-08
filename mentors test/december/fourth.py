def pascal(num):
    if num ==0:# თუ num არის 0,ვაბრუნებთ ცარიელ სიას
        return []
    if num ==1:# თუ num არის 1,ვაბრუნებთ [[1]]
        return [[1]]
    triangle = pascal(num - 1)#ვქმნით სამკუთხედს num-1 რიგამდე
    last = triangle[-1]#ვიღებთ ბოლო რიგს
    new = [1] + [last[i]+ last[i + 1] for i in range(len(last) - 1)] + [1]#ვქმნით ახალ მასივს და ვიგებთ ბოლო რიგის ელემენტების ჯამს
    triangle.append(new)#ვამატებთ ახალ რიგს სამკუთხედში
    return triangle
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(5))
print(pascal(0))