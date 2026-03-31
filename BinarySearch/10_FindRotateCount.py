def count(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i+1
    return 0

def count_optimal(arr):
    s , e = 0 , len(arr)-1

    while s < e:
        mid = (s+e)//2

        if arr[mid] > arr[e]:
            s = mid + 1
        else:
            e = mid

    return s

nums = [5,6,1,2,3,4]
print(count(nums))
print(count_optimal(nums))