def wordBreak(s, word_dct, idx = 0, curr_st = ""):
    if idx == len(s):
        return True


    for i in range(idx, len(s)):
        curr_st += s[i]
        if curr_st in word_dct:

            if wordBreak(s, word_dct, i + 1, ""):
                return True

            curr_st = curr_st[: len(curr_st) -1]

    return False


if __name__ == "__main__":
    st = "takeuforward"
    word_dict = ["take" , "u", "you", "forward"]
    print(wordBreak(st, word_dict))





