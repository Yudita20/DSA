class Solution:
    def removeDuplicates(self,nums):
        i = j = 0
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] , nums[j] = nums[j] , nums[i]
            j += 1

        return  nums

sol = Solution()
num = [1,1,2,2,2,3,3]
print(sol.removeDuplicates(num))
