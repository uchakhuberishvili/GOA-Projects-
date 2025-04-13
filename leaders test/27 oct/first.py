#1) Binary --> Decimal Conversion (2 ქულა)

# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15

# def binary(inputy):
#     res = int(inputy,2)
#     return res
# print(binary("1111"))

# def binary(inputy):
#     return int(inputy,2)
# print(binary("1111"))

def binary(inputy):
    decimal = 0
    for i,d in enumerate(reversed(inputy)):
        if d == '1':
            decimal += 2 ** i
    return decimal
print(binary("1111"))