def peak_elt(arr):
    n = len(arr)

    if n == 1:
        return 0

    if arr[0] > arr[1]:
        return 0

    if arr[n-2] < arr[n-1]:
        return n-1

    low , high = 1 , n-2

    while low <= high:
        mid = (low+high)//2

        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return mid

        elif arr[mid] < arr[mid+1]:
            low = mid + 1

        else:
            high = mid - 1


nums = [1,2,3,4,5,6,4]
print(peak_elt(nums))