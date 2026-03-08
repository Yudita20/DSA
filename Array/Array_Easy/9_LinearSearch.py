def linear_search(arr,target):

    for i in range(0,len(arr)):
        if arr[i] == target:
            return i

    return -1


nums = [1,4,3,5,2,7,8,9]
print(linear_search(nums,4))
