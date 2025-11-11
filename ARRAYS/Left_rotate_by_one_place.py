class Solution:
    # Using slicing
    def rotateByOnePlace(self,nums):
        nums[:] = nums[len(nums)-1:] + nums[:len(nums)-1]
        return nums

    #Using loop
    def rotate(self,nums):
        key = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            nums[i+1] = nums[i]
        nums[0] = key
        return nums

sol = Solution()
num = [55,32,97,-55,45,32,88,21]
print(sol.rotateByOnePlace(num))
print(sol.rotate(num))
