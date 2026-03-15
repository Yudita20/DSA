def next_permutation(arr):
    n = len(arr)-1
    index = -1
    for i in range(n,0,-1):
        if arr[i-1] < arr[i]:
            index = i-1
            break

    if index == -1:
        arr.reverse()
        return arr

    for i in range(n,index,-1):
        if arr[i] > arr[index]:
            arr[i],arr[index] = arr[index],arr[i]
            break

nums = [2,3,1,3,3]
print(next_permutation(nums))


# T(n) : O(n)
# S(n) : O(1)  in-place


