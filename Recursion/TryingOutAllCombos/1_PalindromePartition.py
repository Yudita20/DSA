def palindromeString(s, start, end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return palindromeString(s, start + 1, end - 1)

def palindromePartition(s, index = 0, curr = None, result = None):
    if result is None:
        result = []

    if curr is None:
        curr = []

    if index == len(s):
        result.append(curr.copy())
        return

    for i in range(index, len(s)):
        if palindromeString(s, index, i):
            curr.append(s[index: i+1])
            palindromePartition(s, i + 1, curr, result)
            curr.pop()

    return result


if __name__ == "__main__":
    st = "aabaa"
    print(palindromePartition(st))

