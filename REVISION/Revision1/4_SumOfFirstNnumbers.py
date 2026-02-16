def sum_of_natural_numbers(n):
    #Base case
    if n == 0:
        return 0

    #recursive call
    return n + sum_of_natural_numbers(n-1)



print(sum_of_natural_numbers(5))