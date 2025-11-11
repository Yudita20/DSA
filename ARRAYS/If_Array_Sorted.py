class Solution:
    def ifSorted(self,nums):
        if len(nums) == 0:
            return True
        for i in range(0 , len(nums)-1):
            if not nums[i] < nums[i+1]:
                return False
        return True

sol = Solution()
num = []
print(sol.ifSorted(num))
