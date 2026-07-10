class Python:
    def __init__(self):
        print(end="")

    def fact(self,n):

        if n == 0 or n == 1:
            return 1

        return n * self.fact(n-1)

sol = Python()
print(sol.fact(100))