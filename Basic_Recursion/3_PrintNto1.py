class Python:
    def __init__(self):
        print(end="")

    def print_numbers(self,n):
        if n == 0:
            return
        print(n, end=" ")
        self.print_numbers(n-1)


sol = Python()
sol.print_numbers(5)