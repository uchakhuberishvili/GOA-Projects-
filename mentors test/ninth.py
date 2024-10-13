def product_except_self(nums):
    n = len(nums)
    output = []
    for i in range(n):
        product = 1
        for b in range(n):
            if i != b:
                product *= nums[b]
        output.append(product)
    return output
print(product_except_self([1, 2, 3, 4]))