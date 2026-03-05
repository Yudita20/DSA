def quick_sort(arr,low,high):
    if low >= high:
        return

    pivot_index = partition(arr,low,high)

    quick_sort(arr,low,pivot_index-1)

    quick_sort(arr,pivot_index+1,high)

def partition(arr,start,end):
    pivot = arr[end]
    i = start-1

    for j in range(start,end):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[end] = arr[end],arr[i+1]

    return i+1

nums = [9,4,7,3,1]
quick_sort(nums,0,len(nums)-1)
print(nums)
