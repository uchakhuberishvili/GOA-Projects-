#შექმენით პროგრამა, რომელსაც გადასცემთ სიას, სადაც გექნებათ მთელი რიცხვები. თქვენი დავალებაა,
#რომ ამ სიის ორი მინიმალური რიცხვის ჯამი დააბრუნოთ: ([5, 8, 12, 18, 22]), 13), ([7, 15, 12, 18, 22]), 19), ([25, 42, 12, 18, 22]), 30)


numbers = [20,123,234,54,15]
kvelaze_patara = min(numbers)
numbers.remove(kvelaze_patara)
meore_kvelaze_patara = min(numbers)
ori_kvelaze_patara = kvelaze_patara + meore_kvelaze_patara
print(ori_kvelaze_patara)
