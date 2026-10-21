def averageWaitingTime(bt):
    n = len(bt)
    bt.sort()
    waiting_time = 0
    previous_burst_time = 0

    for i in range(1, n):
        previous_burst_time += bt[i - 1]
        waiting_time += previous_burst_time

    avg_waiting_time = waiting_time // n
    return avg_waiting_time


if __name__ == "__main__":
    arr = [4,1,3,7,2]
    print(averageWaitingTime(arr))