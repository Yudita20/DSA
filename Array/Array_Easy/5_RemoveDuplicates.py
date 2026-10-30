class RemoveDuplicates:

    def __init__(self, nums):
        self.nums = nums
        print("T(n) : O(n)\nS(n) : O(1)\nAPPROACH: TWO POINTERS\ni : Tracks last pos of valid element\nj : scans new elements from the array\n")


    def remove_duplicates(self):
        n = len(self.nums)
        if n == 0:
            return 0

        i = j = 0
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                self.nums[i] = self.nums[j]
            j += 1

        return i + 1

nums = [1, 2, 3, 4]
obj = RemoveDuplicates(nums)
print(obj.remove_duplicates())



