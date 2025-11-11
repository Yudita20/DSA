class Solution:
    def findLargest(self , num):
        largest = float("-inf")
        for element in num:
            if element > largest:
                largest = element
        return largest

sol = Solution()
nums = [55,32,97,-55,45,32,88,21]
print(sol.findLargest(nums))