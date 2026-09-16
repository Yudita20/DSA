def createCombination(l1, l2):
    # Creating a result list that will store the combination
    res = []

    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            res.append(l1[i] + l2[j])

    return res

def letterCombination(s, l_dict, result = None):
    if len(s) == 1:
        return l_dict[int(s)]

    half = len(s) // 2
    list1 = letterCombination(s[0: half],l_dict,result)
    list2 = letterCombination(s[half:len(s)], l_dict, result)

    return createCombination(list1, list2)

if __name__ == "__main__":
    letter_digit_dict = {
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z']
    }

    digit_str = "2"
    print(letterCombination(digit_str, letter_digit_dict))