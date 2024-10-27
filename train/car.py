def reverse(n):
    list = [] #შევქმნათ ცარიელი მასივი,ლისტი,სია
    while n != 0: #ვქმნით ფუნქციას
        list.append(n)
        n = n - 1
    return list

print(reverse(5))

#რისი გაკეთება შეიძლება პითონით
#what can you do with