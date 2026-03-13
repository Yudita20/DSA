def subarraySum_brute(arr):
    max_sum = float("-inf")
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            curr_sum = 0
            for k in range(i,j+1):
                curr_sum += arr[k]

            max_sum = max(max_sum,curr_sum)

    return max_sum

def subarraySum_optimalII(arr):
    max_sum = float("-inf")
    for i in range(0,len(arr)):
        curr_sum = 0
        for j in range(i,len(arr)):
            curr_sum += arr[j]
            max_sum = max(max_sum,curr_sum)

    return max_sum


def subarray_sumKadane(arr):
    curr_sum = 0
    max_sum = float("-inf")

    for i in range(len(arr)):
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


nums = [5,-3,5]
print(f"Max: {subarraySum_brute(nums)}")
print(subarraySum_optimalII(nums))
print(subarray_sumKadane(nums))
