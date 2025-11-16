def _2SumBrute(nums , target):
    for i in range(0 , len(nums)):
        rem = target - nums[i]
        for j in range(i+1 , len(nums)):
            if rem == nums[j]:
                return [i , j]
    return [-1,-1]

    #T(n) : O(n^2)
    #S(n) : O(1)

def _2SumBetter(nums , target):
    hashmap = {}
    for i in range(0 , len(nums)):
        rem = target - nums[i]
        if rem in hashmap:
            return [hashmap[rem] , i]
        hashmap[nums[i]] = i
    return [-1,-1]

    #T(n) : O(n)
    #S(n) : O(n)

def _2SumTwoPointer(nums , target):
    nums.sort()
    i = 0
    j = len(nums)-1
    while i < j :
        sum = nums[i] + nums[j]
        if sum == target:
            return [i , j]
        elif sum < target:
            i += 1
        else:
            j -= 1
    return [-1,-1]

    # T(n) : O(nlogn) + O(n) : O(nlogn)
    # S(n) : O(n) (As we are distorting an original array)


num = [2,6,8,5,11]
tar = 14
print(_2SumBrute(num , tar))
print(_2SumBetter(num , tar))
print(_2SumTwoPointer(num , tar))
