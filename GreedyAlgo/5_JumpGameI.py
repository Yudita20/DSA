def jumpGame(nums):
    n = len(nums)
    max_reach = 0
    for i in range(n):

        if i > max_reach:
            return False

        max_reach = max(max_reach, nums[i] + i)

    return True


if __name__ == "__main__":
    arr = [2,0,1,0]
    print(jumpGame(arr))