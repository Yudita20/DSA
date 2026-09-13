def generateSub(nums, index=0, result = None, current = None):
    if result is None:
        result = []

    if current is None:
        current = []

    if index == len(nums):
        result.append(current)
        return

    #exclude
    generateSub(nums, index+1, result, current)

    generateSub(nums, index+1, result, current + [nums[index]])

    return result

if __name__ == "__main__":
    print(generateSub([1,2,3]))