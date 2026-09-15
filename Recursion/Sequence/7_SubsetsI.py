def subsetsI(arr, index = 0, curr_sum = 0, result = None):
    if result is None:
        result = []


    if index == len(arr):
        result.append(curr_sum)
        return


    subsetsI(arr, index + 1, curr_sum + arr[index], result)
    subsetsI(arr, index + 1, curr_sum, result)

    return result


if __name__ == "__main__":
    print(subsetsI([1]))