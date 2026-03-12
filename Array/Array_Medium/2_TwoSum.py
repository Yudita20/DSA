#Problem: TWO SUM
#Key Approach: HASHMAP
#Stores the values and find if there's exist value which is equals to the difference
# of target and the current element


def brute_two_sum(arr,tar):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            pair_sum = arr[i] + arr[j]
            if pair_sum == tar:
                return [i,j]

    return False
# T(n) : O(n^2)

def optimal_twoSum(arr,tar):
    hash_map ={}
    for i in range(len(arr)):
        pair_sum = tar - arr[i]
        if pair_sum in hash_map:
            return [i,hash_map[pair_sum]]
        hash_map[arr[i]] = i

    return False
# T(n) : O(n)
# S(n) : O(n)

nums = [2,6,5,8,11]
print(brute_two_sum(nums,14))
print(optimal_twoSum(nums,14))