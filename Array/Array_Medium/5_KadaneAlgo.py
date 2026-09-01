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
    curr_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(arr[i] , arr[i] + curr_sum)
        max_sum = max(max_sum, curr_sum)

    return max_sum

nums = [-10,-3,-1]
print(f"Max: {subarraySum_brute(nums)}")
print(subarraySum_optimalII(nums))
print(subarray_sumKadane(nums))
