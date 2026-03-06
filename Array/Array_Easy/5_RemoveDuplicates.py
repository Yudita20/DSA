def remove_duplicates(nums):
    # T(n) : O(n)
    # S(n) : O(1)

    # APPROACH: TWO POINTERS
    # i : Tracks last pos of valid element
    # j : scans new elements from the array

    if len(nums) <= 2:
        return

    i = 0
    for j in range(1,len(nums)):
        if arr[i] != arr[j]:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]


arr = [1,1,2,2,3,3,3]
remove_duplicates(arr)
print(arr)
