def merge_overlap_brute(arr):
    arr.sort()
    res = []
    n = len(arr)
    i = 0

    while i < n:
        start = arr[i][0]
        end = arr[i][1]

        j = i + 1

        while j < n and arr[j][0] <= end:
            end = max(end,arr[j][1])
            j += 1

        res.append([start,end])
        i = j  # Important condition

    return res

def merge_overlap(arr):
    arr.sort()
    res = []

    for interval in arr:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)

        else:
            res[-1][1] = max(res[-1][1] , interval[1])

    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_overlap_brute(intervals))
print(merge_overlap(intervals))