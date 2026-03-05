def insertion_sort(arr,start):
    # Base Case
    if start >= len(arr):
        return

    key = arr[start]
    j = start
    while j>0 and arr[j-1]>key:
        arr[j] = arr[j-1]
        j -= 1

    arr[j] = key

    return insertion_sort(arr,start+1)

nums = [13,46,24,52,20,9]
insertion_sort(nums,1)
print(nums)