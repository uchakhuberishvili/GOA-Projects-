def check_unique(text):
    tot = []
    res = 0
    text = text.lower()
    splitted_text = text.split()#ვსპლიტავთ ჩვენს ტექსტს,დავჭრით და გვექნება მასივი ჩვენი სიტყვების რაც ამ ტექსტშა მოხვედრილი
    for i in splitted_text:#ვუვლით ციკლით დასპლიტულ ტექსტს
        if i not in tot:#თუ ჩვენი ახლანდელი სიტყვა არ არის უკვე tot ცვლადში,დაემატოს
            tot.append(i)#ამით კი ემატება
            res += 1#ამით კი ყოველ დამატებაზე მოიმატოს res ცვლადი 1 ით,რომ დავითვალოთ რამდენი უნიკალური სიტყვა გვაქვს
    return res#ვაბრუნებთ res


print(check_unique("The quick brown fox jumps over the lazy dog"))
print(check_unique("Hello hello world!"))
print(check_unique(""))
print(check_unique("Python is fun. Python is cool."))#მეორე ამოცანის მეოთხე test case-ში 5-ის მაგივრად 4 უნდა იყოს პასუხი
print(check_unique("One word"))