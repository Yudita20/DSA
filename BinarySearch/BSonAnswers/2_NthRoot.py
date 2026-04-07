def root(n,m):
    if m == 0:
        return 0

    low , high = 1 , m

    while low <= high:
        mid = (low+high)//2

        ans = 1
        for _ in range(n):
            ans *= mid
            if ans > m:
                break

        if ans == m:
            return mid
        elif ans < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(root(3,27))
