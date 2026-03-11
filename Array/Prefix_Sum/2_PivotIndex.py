def pivot_index(arr):
    left , right = 0 , sum(arr)
    for i in range(0 , len(arr)):
        right -= arr[i]
        if left == right:
            return i
        left += arr[i]

    return -1

nums = [1,7,3,6,5,6]
print(pivot_index(nums))

# T(n) : O(n)
# S(n) : O(1)
# Left Sum + Current + Right Sum = Total Sum