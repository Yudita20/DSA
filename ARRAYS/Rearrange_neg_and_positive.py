def Rearrange(nums):
    pos=[]
    neg=[]
    result = []
    for i in range(0 , len(nums)):
        if nums[i] > 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    i = 0
    j = 0
    while i<len(pos) and j<len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
    while i<len(pos):
        result.append(pos[i])
        i += 1
    while j<len(neg):
        result.append(neg[j])
        j += 1

    return result


def RearrangeBetter(nums):
    pos = []
    neg = []
    for i in range(0, len(nums)):
        if nums[i] > 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    for i in range(len(nums)//2):
        nums[2*i] = pos[i]
        nums[2*i + 1] = neg[i]

    return nums

def RearrangeOptimal(nums):
    n = len(nums)
    result=[0]*n
    pos_index = 0
    neg_index = 1
    for i in range(0 , len(nums)):
        if nums[i] > 0:
            result[pos_index] = nums[i]
            pos_index += 2
        else:
            result[neg_index] = nums[i]
            neg_index += 2
    return result


# num = [1,2,-4,-5]
num = [-6,-2,1,4,3,-5]
print(RearrangeOptimal(num))