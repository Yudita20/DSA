def combinationSumIII(n, k, idx = 1, curr_sum = 0, curr = None, result = None):
    if result is None:
        result = []

    if curr is None:
        curr = []

    if len(curr) == k:
        if curr_sum == n:
            result.append(curr.copy())
            return


    for i in range(idx, 10):
        curr.append(i)
        combinationSumIII(n, k, i+1, curr_sum + i, curr, result)
        curr.pop()

    return result


if __name__ == "__main__":
    print(combinationSumIII(9, 3))

