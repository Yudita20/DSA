class Python:
    def __init__(self):
        print(end="")

    def sum_n_numbers(self,n,sum):
        # Base case
        if n == 0:
            return sum

        return self.sum_n_numbers(n-1,sum+n)



sol = Python()
print(sol.sum_n_numbers(5,0))
