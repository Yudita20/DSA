def sortIntegers(arr):
    arr.sort(key=lambda x: (x.bit_count(), x))
    return arr

if __name__ == "__main__":
    nums = [5,2,3,8]
    print(sortIntegers(nums))
