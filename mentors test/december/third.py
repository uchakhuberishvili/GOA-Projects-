def reverse_order(text1):
    res = []
    splitted = text1.split()#ვსპლიტავთ ჩვენს ტექსტს,დავჭრით და გვექნება მასივი ჩვენი სიტყვების რაც ამ ტექსტშა მოხვედრილი
    for i in splitted[::-1]: #ვუვლით ჩვენს დაჭრილ,დაჩეხილ,დანა დარტყმულ მასივ უკუღმა
        res.append(i)#და ვამატებთ რეს მასივს ყველა სიტყვას,ბოლოდან დაწყებული პირველიდან დამთავრებული
    return ' '.join(res)#დავაჯოინებთ,ვაქცევთ სტრინგად
print(reverse_order("sigma boy"))
print(reverse_order("Hello World"))
print(reverse_order("Python is great"))
print(reverse_order("a b c"))
print(reverse_order(""))
print(reverse_order(" Spaces "))

