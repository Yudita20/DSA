def move_zeroes(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            # We encounter the first zero in the array
            break
        i += 1

    #  If no zeroes found
    if i == 0:
        return

    for j in range(i+1,len(arr)):
        if arr[j] != 0:
            # Swap the first zero with the next non-zero element
            arr[i],arr[j] = arr[j],arr[i]
            i += 1


nums = [1,0,2,3,0,4,0,1]
move_zeroes(nums)
print(nums)

# T(n) : O(n)
# S(n) : O(1)