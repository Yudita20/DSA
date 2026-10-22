def jobScheduling(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[2],reverse = True)
    max_slot = max(j[1] for j in jobs)

    #Create a slot list
    slot = [False] * max_slot
    cnt = 0
    profit = 0

    for i in range(n):
        r = jobs[i][1]
        scheduled = False

        for j in range(min(r, max_slot)-1, -1, -1):
            if not slot[j]:
                slot[j] = True
                scheduled = True
                break

        if scheduled:
            cnt += 1
            profit += jobs[i][2]

    return [cnt, profit]


if __name__ == "__main__":
    job = [[1,2,100], [2,1,19], [3,2,27], [4,1,25], [5,1,15]]
    print(jobScheduling(job))

