def brute(arr):
    min_elt = float("+inf")
    max_profit = 0
    i = 0
    while i < len(arr):
        if arr[i] < min_elt:
            min_elt = arr[i]

        max_profit = max(max_profit , arr[i]-min_elt)
        i += 1
    return max_profit

nums = [2,4,1]
print(brute(nums))