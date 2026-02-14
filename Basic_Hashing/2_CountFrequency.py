def hashing(arr):
    hash_map = {}
    for i in range(0,len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i] , 0) + 1

    print(hash_map)

arr = [2,2,3,4,4,2]
hashing(arr)

