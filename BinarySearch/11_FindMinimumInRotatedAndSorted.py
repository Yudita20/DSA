def minimum_in_rotated(arr):
    left , right = 0 ,len(arr)-1

    while left < right:
        mid = (left + right)//2

        if arr[mid] > arr[right]:
            left = mid + 1

        elif arr[mid] < arr[right]:
            right = mid

        else:
            right -= 1

    return arr[left]

nums = [4,5,6,7,0,1,2,3]
print(minimum_in_rotated(nums))

# T(n) : O(log n) (best case)  and O(n) (worst case)
                                   #[2,2,2,2,2]

