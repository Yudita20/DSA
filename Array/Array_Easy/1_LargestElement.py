def largest_element(arr,low,high):
    largest = float("-inf")

    for i in range(low,high):
        if arr[i] > largest:
            largest = arr[i]

    return largest

nums= [3,3,6,1]
print(f"Largest : {largest_element(nums,0,len(nums))}")

