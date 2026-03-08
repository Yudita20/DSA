# Approach: TWO POINTER
def union_sorted_array(arr1,arr2):
    # Used two pointer for sorted array
    # T(n) : O(n + m)
    # S(n) : O(n+m)

    res = []
    i = j = 0

    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            if len(res) == 0 or arr1[i] != res[-1]:
                res.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            if len(res) == 0 or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1
        else:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1

    while i<len(arr1):
        if len(res) == 0 or res[-1] != arr1[i]:
            res.append(arr1[i])
            i += 1

    while j<len(arr2):
        if len(res) == 0 or res[-1] != arr2[j]:
            res.append(arr2[j])
            j += 1

    return res


# Approach : Hashing
def map_union(arr1,arr2):
    # Used when the array is unsorted
    # T(n) : O(n + m)  Average time for insertion in dict is O(1)
    # S(n) : O(n+m)

    res = []
    freq = {}
    for i in range(len(arr1)):
        # No need to count frequency for finding unique keys
        # freq[arr1[i]] = freq.get(arr1[i], 0) + 1
        freq[arr1[i]] = True

    for j in range(len(arr2)):
        # freq[arr2[j]] = freq.get(arr2[j], 0) + 1
        freq[arr2[j]] = True


    for keys in freq.keys():
        res.append(keys)

    return res


num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [2,3,4,4,5,11,12]
print(union_sorted_array(num1,num2))
print(map_union(num1,num2))


