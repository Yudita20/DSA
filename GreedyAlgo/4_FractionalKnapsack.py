def knapsack(val, wt, cap):
    items = sorted(zip(val, wt), key=lambda x: x[0] / x[1], reverse=True)

    total_val = 0
    i = 0
    while cap > 0 and i < len(items):
        if items[i][1] <= cap:
            total_val += items[i][0]
            cap -= items[i][1]
        else:
            total_val += (items[i][0] / items[i][1]) * cap
            cap = 0
        i += 1

    return round(total_val, 6)


if __name__ == "__main__":
    value = [10, 20, 30]
    weight = [5, 10, 15]
    print(knapsack(value, weight, 20))

