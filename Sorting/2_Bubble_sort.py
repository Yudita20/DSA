def bubble_sort(arr):
    initial_sorted = True
    for i in range(len(arr)-1,-1,-1):
        swap = 0
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap += 1
        #Check swap for 1 pass
        if i == len(arr)-1 and swap>0:
            initial_sorted = False

    #Already sorted
    if initial_sorted:
        print("Already sorted")
        return arr

    return arr


nums = [10,3,45,62]
print(bubble_sort(nums))



