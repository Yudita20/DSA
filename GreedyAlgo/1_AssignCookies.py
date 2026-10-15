def assignCookies(g, s):
    g.sort()
    s.sort()

    n, m = len(g), len(s)
    cnt = 0
    i = j = 0
    while i < n and j < m:
        if s[j] >= g[i]:
            cnt += 1
            i += 1
            j += 1
        elif g[i] > s[j]:
            j += 1

    return cnt


if __name__ == "__main__":
    nums = [1,2,3]
    size = [1,1,3]
    print(assignCookies(nums, size))