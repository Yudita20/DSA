class Solution:
    def findLargest(self , nums):
        largest = float("-inf")
        for num in nums:
            if num > largest:
                largest = num
        return largest

sol = Solution()
num = [55,32,97,-55,45,32,88,21]
print(sol.findLargest(num))