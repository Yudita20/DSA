def rotate(nums , k):
    rot = k % len(nums)
    while rot > 0 :
        key = nums[len(nums)-1]
        for i in range(len(nums)-1 , 0 , -1):
            nums[i] = nums[i-1]
        nums[0] = key
        rot -= 1
    return nums
    #T(n) : O(n^2)
    #S(n) : O(1)


def rotateInsert(nums , k):
    rot = k % len(nums)
    for _ in range(0 , rot):
        e = nums.pop()
        nums.insert(0 , e)
    return nums
    # T(n) : O(n*rot)
    # S(n) : O(1)

def rotateSlicing(nums , k):
    rot = k % len(nums)
    nums[:] = nums[len(nums)-rot:] + nums[:len(nums)-rot]
                #O(k)                O(n-k)
    return nums
    # T(n) : O(k) + O(n-k) : O(n)
    # S(n) : O(1)

def reverse(nums , left , right):
    while left < right:
        nums[left] , nums[right] = nums[right] , nums[left]
        left += 1
        right -= 1

def rotateReverse(nums , k):
    rot = k % len(nums)
    reverse(nums,0,len(nums) - rot - 1)  #O((n-rot)/2)
    reverse(nums , len(nums)-rot , len(nums)-1)  #O(rot/2)
    reverse(nums , 0 , len(nums)-1)  #O(n/2)
    return nums
    # T(n) : O(n)
    # S(n) : O(1)

num = [1,2,3,4,5,6]
d = 3
# print(rotate(num , d))
# print(rotateInsert(num  ,d))
# print(rotateSlicing(num , d))
# print(rotateReverse(num , d))