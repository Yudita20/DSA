def minimum_in_rotated(arr):
    left , right = 0 ,len(arr)-1

    while left < right:
        mid = (left + right)//2

        if arr[mid] > arr[right]:
            left = mid + 1

        else:
            right = mid

    return arr[left]

nums = [4,5,6,7,0,1,2,3]
print(minimum_in_rotated(nums))