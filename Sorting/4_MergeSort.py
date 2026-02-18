def merge_sort(arr,start,end):
    if start >= end:
        return

    mid = start + (end - start) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)

def merge(arr,start,mid,end):
    i = start
    j = mid+1
    temp = []

    while i<=mid and j<=end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i<=mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    for i in range(start,end+1):
        arr[i] = temp[i-start]

nums = [3, 2, 8, 5, 1, 4, 23]
merge_sort(nums, 0, len(nums) - 1)
print(nums)




