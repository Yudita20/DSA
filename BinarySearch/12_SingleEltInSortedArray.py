def single_elt(arr):
    left , right = 0 ,len(arr)-1

    while left < right:
        mid = (left+right)//2

        if (mid%2 ==0 and arr[mid] == arr[mid+1]) or (mid%2 == 1 and arr[mid] == arr[mid-1]):
            left = mid + 1

        else:
            right = mid

    return arr[left]

nums = [1,1,3,5,5]
print(single_elt(nums))