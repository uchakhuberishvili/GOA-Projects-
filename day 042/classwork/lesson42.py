# Original string
original = "Hello, World!"
reversedd = ""

for i in range(len(original) - 1, -1, -1):
    reversedd += original[i]

print(reversedd)