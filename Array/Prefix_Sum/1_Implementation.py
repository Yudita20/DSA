# LEETCODE:724

def prefix_sum_basics(arr):
    # Creating prefix sum array of length similar to original array
    prefix_sum = [0]*len(arr)

    # First element is same in both the arrays
    prefix_sum[0] = arr[0]

    for i in range(len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    return prefix_sum

def range_sum(sum_array,l,r):
    if l == 0:
        return sum_array[r]

    return sum_array[r] - sum_array[l-1]

def prefix_sum2(arr):
    prefix_sum = [0]*len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1,len(arr)):
        prefix_sum[i] = prefix_sum[i-1]+arr[i]
    return prefix_sum

def range_sum2(arr,l,r):
    return arr[r+1] - arr[l]

nums = [2,4,1,5,3]
new_nums = [0]*(len(nums)+1)
for i in range(1,len(nums)+1):
    new_nums[i] = nums[i-1]

print(prefix_sum_basics(nums))
print(f"Sum in range from 1 to 3 is : {range_sum(prefix_sum_basics(nums),1,3)}")
print(prefix_sum2(new_nums))
print(f"Sum in range from 1 to 3 is : {range_sum2(prefix_sum2(new_nums),1,3)}")