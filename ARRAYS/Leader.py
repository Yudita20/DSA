def leader(nums):
    max_element = nums[-1]
    result = []
    for i in range(len(nums)-1 , -1 , -1):
        if nums[i] >= max_element:
            result.append(nums[i])
        max_element = max(max_element, nums[i])

    return result[::-1]


num =  [4,7,1,0,6]
ans = leader(num)
for leader in ans:
    print(leader , end=" ")

#T(n) : O(n)
#S(n) : O(n)(Overall space)