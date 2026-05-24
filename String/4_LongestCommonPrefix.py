def longest_common(arr):
    n = len(arr)
    curr_base = arr[0]
    for i in range(1 , n):
        j = 0
        length = min(len(curr_base) , len(arr[i]))
        while j < length:
            if curr_base[j] != arr[i][j]:
                break
            j += 1
        curr_base = curr_base[0:j]

    return curr_base

# org_arr = ["flowers" , "flow" , "fly" , "flight"]
org_arr = ["lady" , "lazy"]
# org_arr = ["dog" , "cat" , "animal" , "monkey"]
print(longest_common(org_arr))

