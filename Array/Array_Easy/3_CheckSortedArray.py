def sorted_array(arr,low,high):
    # TC:O(N)
    # SC:O(1)

    for i in range(low,high-1):
        if arr[i] > arr[i+1]:
            return False

    return True


nums = [3,3,6]
print(sorted_array(nums,0,len(nums)))






