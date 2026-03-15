def longest_sequence(arr):
    if len(arr) == 0:
        return 0

    arr.sort()
    count = 1
    max_count = count
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        elif arr[i]!=arr[i+1] and (arr[i+1] == arr[i] + 1):
            count += 1
            max_count = max(max_count,count)
        else:
            count = 1
            max_count = max(max_count, count)

    return max_count

# T(n) : O(nlogn)
# S(n) : O(1)

def optimal_set(arr):
    if len(arr) == 0:
        return 0

    longest = 1
    st = set(arr)

    for j in st:
        if j-1 not in st:
            count = 1
            var = j

            while var+1 in st:
                count += 1
                var += 1

            longest = max(longest,count)

    return longest

# T(n) : O(n)
# S(n) : O(n)

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longest_sequence(nums))
print(optimal_set(nums))