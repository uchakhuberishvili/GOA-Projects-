# 2) Decimal --> Binary Conversion (2 ქულა)

# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111

def decimal(inputy):
    binary = ""
    while inputy > 0:
        binary = str(inputy % 2) + binary
        inputy //= 2
    return binary if binary else "0"
print(decimal(15))