def andOperation(left, right):
    result = 0
    count = 0

    while left != right:
        left >>= 1
        right >>= 1
        count += 1

    result |= left << count
    return result

if __name__ == "__main__":
    print(andOperation(8, 11))