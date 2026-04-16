def student_count(nums , pages):
    student = 1
    pages_count = 0

    for page in nums:
        if pages_count + page <= pages:
            pages_count += page
        else:
            student += 1
            pages_count = page
    return student

def book_allocation(nums , m):
    if len(nums) < m:
        return -1

    low , high = max(nums) , sum(nums)
    while low <= high:
        mid = (low + high) // 2
        if student_count(nums , mid) > m:
            low = mid + 1
        else:
            high = mid - 1
    return low


arr = [15,17,20]
print(book_allocation(arr , 2))