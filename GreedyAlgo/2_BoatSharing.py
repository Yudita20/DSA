def assignCookies(weight, limit):
    weight.sort()
    i = 0
    j = len(weight) - 1

    boats = 0
    while i < j:
        if weight[i] + weight[j] > limit:
            boats += 1
            j -= 1
        else:
            boats += 1
            i += 1
            j -= 1

    if i == j:
        boats += 1

    return boats


if __name__ == "__main__":
    people_weights = [3,2,1,4]
    print(assignCookies(people_weights, 4))
