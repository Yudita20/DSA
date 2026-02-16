def print_freq(arr):
    freq_map = {}
    for i in range(0,len(arr)):
        freq_map[arr[i]] = freq_map.get(arr[i],0)+1

    for i in range(0,len(arr)):
        if freq_map[arr[i]]== 1:
            return arr[i]
    return -1



arr = [4,5,1,2,0,4]
print(print_freq(arr))

#Can we do this in one pass?
#No,because we need to know the complete knowledge about frequency before deciding uniqueness
