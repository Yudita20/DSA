def reverse(arr,left,right):
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1


def rotate_by_k(arr,k):
    n = len(arr)
    rot = k % n

    reverse(arr,0,rot)
    reverse(arr,rot+1,len(arr)-1)
    reverse(arr,0,len(arr)-1)


nums = [1,2,3,4,5,6,7]
rotate_by_k(nums,3)
print(nums)

# T(n) : O(n)
# S(n) : O(1)