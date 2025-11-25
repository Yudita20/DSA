def Brute(nums):
    max_sum = float("-inf")
    for i in range(0 , len(nums)):
        for j in range(0 , len(nums)):
            sum = 0
            for k in range(i , j+1):
                sum += nums[k]
                max_sum = max(max_sum , sum)
    return  max_sum
    #T(n) = O(n^3)
    #S(n) = O(1)

def Better(nums):
    max_sum = float("-inf")
    for i in range(0 , len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            max_sum = max(max_sum , sum)
    return max_sum
    #T(n) = O(n^2)
    #S(n) = O(1)


def Optimal(nums):
    #Kadane Algorithm
    max_sum = float("-inf")
    sum = 0
    for i in range(0 , len(nums)):
        sum += nums[i]
        max_sum = max(max_sum , sum)
        if sum <0:
            sum = 0
    return max_sum
    #T(n) = O(n)
    #S(n) = O(1)

num = [-2,1,-3,4,-1,2,1,-5,4]
# print(Brute(num))
# print(Better(num))
print(Optimal(num))


