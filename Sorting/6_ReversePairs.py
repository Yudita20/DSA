def merge_sort(arr,start,end):
    if start >= end:
        return 0

    mid = start + (end - start) // 2
    count = 0
    count += merge_sort(arr, start, mid)
    count += merge_sort(arr, mid + 1, end)
    count += count_reverse_pairs(arr,start,mid,end)
    merge(arr, start, mid, end)

    return count

def count_reverse_pairs(arr,start,mid,end):
    count = 0
    j = mid+1
    for i in range(start,mid+1):
        while j<=end and arr[i]>2*arr[j]:
            j += 1

        count += j - (mid+1)
    return count


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
print(merge_sort(nums, 0, len(nums) - 1))
print(nums)




