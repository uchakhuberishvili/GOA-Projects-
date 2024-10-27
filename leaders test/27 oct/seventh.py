# 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]
def fib(num):
    seq = [0, 1]
    for i in range(2, num):
        seq.append(seq[-1] + seq[-2])
    return seq[:num]
print(fib(5))
print(fib(7))
print(fib(20))