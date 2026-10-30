class SecondLargestElement:

    def __init__(self, arr):
        self.arr = arr
        print("Time complexity is O(n)\nSpace complexity is O(1)")

    def second_largest_brute(self):
        largest = float("-inf")
        second_largest = float("-inf")
        n = len(self.arr)
        for i in range(n):
            if self.arr[i] > largest:
                largest = self.arr[i]

        for i in range(n):
            if self.arr[i] > second_largest and self.arr[i] != largest:
                second_largest = self.arr[i]

        second_largest = second_largest if second_largest != float("-inf") else -1
        return second_largest

    def second_largest_optimal(self):
        largest = float("-inf")
        second_largest = float("-inf")
        n = len(self.arr)
        for i in range(n):
            if self.arr[i] > largest:
                second_largest = largest
                largest = self.arr[i]
            elif self.arr[i] > second_largest and self.arr[i] != largest:
                second_largest = self.arr[i]

        second_largest = second_largest if second_largest != float("-inf") else -1
        return second_largest


nums = [-2, -1]
obj = SecondLargestElement(nums)
print(obj.second_largest_brute())
print(obj.second_largest_optimal())



