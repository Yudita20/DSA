def bubble_sort(arr,start,end):
    low = start
    # Length of the array will remain same
    # if len(arr) == 1:
    #     return

    # BASE CASE
    if start >= end:
        return

    # OR
    # if end == 0:
    #     return

    # WORK
    while low < end:
        if arr[low] > arr[low+1]:
            arr[low],arr[low+1] = arr[low+1],arr[low]
        low += 1

    # RECURSIVE CALL
    return bubble_sort(arr,start,end-1)

nums = [13,46,24,52,20,9]
bubble_sort(nums,0,len(nums)-1)
print(nums)