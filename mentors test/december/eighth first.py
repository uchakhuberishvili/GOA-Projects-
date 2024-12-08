def smallest(arr,k):
    arr = sorted(arr)#ვალაგებთ ჩვენს ლისტს
    return arr[k-1]#ვაბრუნებთ arr დან მე-(k-1)-ე ინდექსზე მყოფ რიცხვს
print(smallest([3, 2, 1, 5, 6, 4],2))
print(smallest([3, 2, 1, 5, 6, 4],4))
print(smallest([7, 10, 4, 3, 20, 15],3))
print(smallest([1, 2, 3, 4, 5],1))
print(smallest( [1, 2, 3, 4, 5],5))