def bubble_sort(arr):
    for i in range(len(arr)-1,-1,-1):
        swap = 0
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap += 1

        #Check swap for 1 pass
        if i == len(arr)-1 and swap == 0:
            return arr

    return arr


nums = [1,2,3,4,5]
print(bubble_sort(nums))
