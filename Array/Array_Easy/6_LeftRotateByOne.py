def left_rotate(arr):
    key = arr[0]

    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1]

    arr[-1] = key

nums = [-1,0,3,6]
left_rotate(nums)
print(nums)
