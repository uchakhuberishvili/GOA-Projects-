# შევქმენით ფუნქცია
def smaller(arr):
     # შექმენით ცარიელი სია result-ი, სადაც ვინახავთ ყველა რიცხვისთვის რამდენი ელემენტი არის მეტი.
    result = []
     # დავადგინოთ ელემენტების რაოდენობა.
    count = 0
    # გავაკეთოთ ციკლი რომელიც შექმნის დიაპაზონს რომელიც გადაუვლის arr-ს. 
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  
            # თუ arr[i] მეტია arr[j] - ზე, მაშინ გავიმეოროთ count.
            if arr[i] > arr[j]:
                count += 1
        # დავუმატოთ count-ი result-ში.
        result.append(count)  # დავუმატოთ count-ი result-ში.
        # გავისართოთ count-ი დაწყებული სიდიდის მერე.
        count = 0  
    # დაბრუნდით შედეგს.
    return result  
