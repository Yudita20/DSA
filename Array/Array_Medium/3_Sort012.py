# Problem : Sort array of 0,1,2
# Approach : DUTCH NATIONAL FLAG ALGORITHM


def brute_force(arr):
    nums = [None]*len(arr)
    for i in range(len(arr)):
        nums[i] = arr[i]

    nums.sort()
    return nums

def brute2(arr):
    temp_zero = []
    temp_one = []
    temp_two = []
    for i in range(len(arr)):
        if arr[i] == 0:
            temp_zero.append(arr[i])
        elif arr[i] == 1:
            temp_one.append(arr[i])
        else:
            temp_two.append(arr[i])

    j = 0
    i = 0
    while i<len(temp_zero):
        if j<len(arr):
            arr[j] = temp_zero[i]
            i += 1
            j += 1
    i = 0
    while i<len(temp_one):
        if j<len(arr):
            arr[j] = temp_one[i]
            i += 1
            j += 1

    i = 0
    while i < len(temp_two):
        if j < len(arr):
            arr[j] = temp_two[i]
            i += 1
            j += 1

def optimal_solution(arr):
    low = mid = 0
    high = len(arr)-1

    #0 to left-1 -> 0
    #left to mid-1 -> 1
    #mid to high -> random values
    #high+1 to end -> 2

    while mid < high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1

    return arr


org_arr = [1,0,2,1,0]
# print(brute_force(org_arr))
# brute2(org_arr)
# print(org_arr)
print(optimal_solution(org_arr))
