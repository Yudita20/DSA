def leader(arr):
    n = len(arr)-1
    max_elt = arr[n]
    res = [max_elt]
    for i in range(n-1,-1,-1):
        if arr[i] > max_elt:
            max_elt = max(arr[i],max_elt)
            res.append(arr[i])

    res.reverse()
    return res

nums = [16,17,4,3,5,2]
print(leader(nums))


# T(n) : O(n)
# S(n) : O(1)