def maximum_product(arr):
    n = len(arr)
    max_pdt = float("-inf")
    prefix , suffix = 1 , 1

    for i in range(n):
        if prefix == 0:
            prefix = 1

        if suffix == 0:
            suffix = 1

        prefix *= arr[i]

        suffix *= arr[n-i-1]

        max_pdt = max(max_pdt,prefix,suffix)

    return max_pdt

nums = [4, 5, 3, 7, 1, 2]
print(maximum_product(nums))