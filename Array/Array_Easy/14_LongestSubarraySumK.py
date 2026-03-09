def longest_subarray(arr,k):
    max_length = 0
    for i in range(len(arr)):
        length = 0
        sums = 0

        for j in range(i , len(arr)):
            sums += arr[j]
            length += 1
            if sums == k:
                max_length = max(length , max_length)

    return max_length

def longest_sub_array(arr , k):
    left = 0
    max_length = 0
    curr_sum = 0
    for right in range(len(arr)):
        curr_sum += arr[right]

        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        if curr_sum == k:
            length = right - left + 1
            max_length = max(length,max_length)
            right += 1

    return max_length


nums = [10,5,2,7,1,9]
k = 15
print(longest_sub_array(nums,k))
