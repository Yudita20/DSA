import math
def majorityElementBrute(nums):
    for i in range(0 , len(nums)):
        freq = 1
        for j in range(i+1 , len(nums)):
            if nums[i] == nums[j]:
                freq += 1
        if freq > math.floor(len(nums) // 2):
            return nums[i]


def majorityElement(nums):
    hashmap = {}
    for i in range(0 , len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i] , 0) + 1
    for key , value in hashmap.items():
        if value > math.floor((len(nums)//2)):
            return key

def majorityBetter(nums):
    nums.sort()
    freq = 1
    if len(nums) == 0:
        return 0
    for i in range(0 , len(nums)-1):
        if nums[i] == nums[i+1]:
            freq += 1
            if freq > math.floor((len(nums)//2)):
                return nums[i]


def majorityElementOptimal(nums):
    candidate = nums[0]
    count = 1
    for i in range(1 , len(nums)):
        if count == 0:
            candidate = nums[i]
            count += 1
        else:
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
    return candidate
    #We don't need to verify because majority element will always exist.
    #Otherwise , we can use the verification code below to verify the majority element
    # cnt_candidate = 0
    # for i in range(0 , len(nums)):
    #     if nums[i] == candidate:
    #         cnt_candidate += 1
    #
    # if cnt_candidate > math.floor(len(nums)//2):
    #     return candidate
    # else:
    #     return -1
num = [3,2,3]
print(majorityElementBrute(num))
print(majorityElement(num))
print(majorityBetter(num))
print(majorityElementOptimal(num))