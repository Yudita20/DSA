class Solution:
    def findSecondLargestBrute(self,nums):
        largest = float("-inf")
        second_largest = float("-inf")
        for num in nums:
            if num > largest:
                largest = num

        for num in nums:
            if num>second_largest and num!=largest:
                second_largest = num
        return second_largest

    def findSecondLargestOpti(self , nums):
        largest = float("-inf")
        second_largest = float("-inf")
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num!=largest:
                second_largest = num
        return second_largest

sol = Solution()
num = [55,32,97,-55,45,32,88,21]
print(sol.findSecondLargestBrute(num))
print(sol.findSecondLargestOpti(num))