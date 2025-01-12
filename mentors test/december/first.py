def anagram(text1,text2):
    text1 = text1.replace(" ","").lower()#replace ით ვაშორებთ ცარიელ ადგილებს და lower  ით ვაპატარავებთ ყველა ასოს
    text2 = text2.replace(" ","").lower()
    return sorted(text1) == sorted(text2)#ვამოწმებთ ემთხვევა თუ არა დალაგებული სტრინგები ერთმანეთს
print(anagram("listen","silent"))
print(anagram("triangle","integral"))
print(anagram("apple","pale"))
print(anagram("a","a"))
print(anagram("rat","car"))