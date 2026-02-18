def count_inversion_brute(arr):
    count_inv = 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count_inv += 1

    return count_inv


def count_inversion(arr,start,end):
    if start >= end:
        return 0

    inv_count = 0
    mid = (start+end)//2
    inv_count += count_inversion(arr,start,mid)
    inv_count += count_inversion(arr, mid+1,end)
    inv_count += merge(arr, start, mid , end)

    return inv_count

def merge(arr,start,mid,end):
    inv_count = 0
    i = start
    j = mid + 1
    temp = []

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += mid-i+1
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    for i in range(start, end + 1):
        arr[i] = temp[i - start]

    return inv_count

nums = [3, 1, 2]
# print(count_inversion_brute(nums))
print(count_inversion(nums,0,len(nums)-1))

