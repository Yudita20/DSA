def sortArray(num):
    num.sort()
    return num
    #T(n) : O(nlogn)
    #S(n) : O(1)

def sortArrayBetter(num):
    c0 = c1 = c2 = 0
    for i in range(0 , len(num)):
        if num[i] == 0:
            c0 += 1
        elif num[i] == 1:
            c1 += 1
        else:
            c2 += 1

    for i in range(0 ,c0):
        num[i] = 0
    for i in range(c0,c0+c1):
        num[i] = 1
    for i in range(c0+c1 , len(num)):
        num[i] = 2
    return num
    # T(n) : O(n) + O(n) : O(n)
    # S(n) : O(1)

def sortArrayOptimal(num):
    low = 0
    mid = 0
    high = len(num)-1
    while mid <= high:
        if num[mid] == 0:
            num[mid] , num[low] = num[low] , num[mid]
            low += 1
            mid += 1
        elif num[mid] == 1:
            mid += 1
        else:
            num[mid] , num[high] = num[high] , num[mid]
            high -= 1
    return num
    #T(n) : O(n)
    #S(n) : O(1)


nums = [2,0,2,1,1,0]
# print(sortArray(nums))
# print(sortArrayBetter(nums))
# print(sortArrayBetter(nums))