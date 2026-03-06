def second_largest1(arr,low,high):
    #TC:O(2*N)
    #SC:O(1)

    largest = float("-inf")

    for i in range(low,high):
        if arr[i]>largest:
            largest = arr[i]

    print(largest)

    second = float("-inf")
    for i in range(low,high):
        if (arr[i] > second) and (arr[i] != largest):
            second = arr[i]

    return second

def second_largest(arr,low,high):
    # TC:O(N)
    # SC:O(1)

    largest = float("-inf")
    second = float("-inf")

    for i in range(low,high):
        if arr[i] >= largest:
            second = largest
            largest = arr[i]

        elif arr[i]>second and arr[i] != largest:
            second = arr[i]

    return second


nums = [3,3,6,1]
print(f"Second Largest : {second_largest(nums,0,len(nums))}")