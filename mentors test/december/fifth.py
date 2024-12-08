def cipher(text, th):
    result = ''# ცარიელი სტრინგი სადაც შეინახება საბოლოო შედეგი
    for i in text:
        if i.isalpha():#ვამოწმებთ ანუ არის თ არა ასო,ეს სიმბოლო ანბანის ასო
            b = 'A' if i.isupper() else 'a'#ვადგენთ დიდი ასოა თუ პატარა
            result += chr((ord(i) - ord(b) + th)% 26 + ord(b))#ვქმნით ანბანის საწყის მნიშვნელობას ანუ A აბ a,ord ფუნქციის გამოყენებით,შემდეგ ვამატებთ th ს მნიშვნელობას,ვასრულებთ 26,რომ ასოები დარჩეს 26 ასოს შგნით,ვუმატებთ საწყისს მნიშვნელობას b,ord-ით,რომ დავაბრუნოთ ასო
        else:
            result += i#თუ სიმბოლო არა არის ასო მაშინ პირდაპირ ვამატებთ შედეგს
    return result
print(cipher("abc", 2))
print(cipher("xyz", 3))
print(cipher("Hello, World!", 5))
print(cipher("Python", 0))
print(cipher("abc", -1))