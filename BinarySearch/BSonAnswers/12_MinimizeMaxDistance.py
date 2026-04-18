import math

def minimize_max_dis(nums , k):
    n = len(nums)
    how_many = [0]*(n-1)

    for _ in range(k):
        max_section = -1
        max_idx = -1

        for i in range(n-1):
            diff = nums[i+1] - nums[i]
            section_length = diff / (how_many[i] + 1)

            if section_length > max_section:
                max_section = section_length
                max_idx = i

        how_many[max_idx] += 1


    max_ans = -1
    for i in range(n-1):
        diff =nums[i+1] - nums[i]
        section_length = diff / (how_many[i] + 1)
        max_ans = max(max_ans , section_length)

    return max_ans


# Method2
def count_gas_station(nums ,dis):
    count = 0

    for i in range(len(nums)-1):
        gap = nums[i+1] - nums[i]
        num_in_btw = math.ceil(gap/dis) - 1
        count += num_in_btw

    return count


def minimize_max_distance(nums , k):
    low = 0
    high = max(nums[i+1] - nums[i] for i in range(len(nums)-1))

    diff = 1e-6
    while high-low > diff:
        mid = (low+high)/2

        if count_gas_station(nums ,mid) > k:
            low = mid
        else:
            high = mid

    return high
arr = [1,2,3,4,5,6,7,8,9,10]
print(minimize_max_distance(arr , 10))

