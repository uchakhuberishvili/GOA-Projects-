names = ["ucha", "gio", "luka", "Data", "nica"]
index = int(input("Enter a number from 0 to 4: "))
if 0 <= index < len(names):
    print(f"The element at index {index} is: {names[index]}")
else:
    print("enter a number between 1-5")
