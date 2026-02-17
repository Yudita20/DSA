#Approach:Selection sort
#TC(n):O(N^2)
#SC(n):O(1)
#Stable sort:No

def selection_sort(nums):
    swap = 0
    for i in range(0,len(nums)):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j

        # If the array is already sorted then it will not do any swaps
        if min_index != i:
            nums[i],nums[min_index] = nums[min_index] , nums[i]
            swap += 1

    return f"{nums} , {swap}"

arr = [1,2,3,4,5,6]
print(selection_sort(arr))
