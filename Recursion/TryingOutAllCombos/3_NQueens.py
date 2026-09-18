def isValid(board, n, row, col):
    i = row - 1
    while i >= 0:
        if board[i][col] == "Q":
            return False

        i -= 1

    # diagonal-right
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False

        i -= 1
        j += 1


    # Diagonal-left
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False

        i -= 1
        j -= 1
    # Return true if safe
    return True

def placeQueens(board, n, row, result = None):
    if result is None:
        result = []

    if row >= n:
        temp = ["".join(col) for col in board]
        result.append(temp)
        return

    for col in range(0, n):
        if isValid(board, n, row, col):
            board[row][col] = "Q"

            placeQueens(board, n, row + 1, result)

            board[row][col] = "."

    return result


def placeQueensOptimal(board, n, row, col_set, diagonal_set, anti_diagonal_set, result=None):
    if result is None:
        result = []

    if row >= n:
        temp = ["".join(col) for col in board]
        result.append(temp)
        return

    for col in range(n):
        diagonal = row + col
        anti_diagonal = row - col

        if (col in col_set) or (diagonal in diagonal_set) or (anti_diagonal in anti_diagonal_set):
            continue

        col_set.add(col)
        anti_diagonal_set.add(anti_diagonal)
        diagonal_set.add(diagonal)

        board[row][col] = "Q"

        placeQueensOptimal(board, n, row + 1, col_set, diagonal_set, anti_diagonal_set, result)

        col_set.discard(col)
        anti_diagonal_set.discard(anti_diagonal)
        diagonal_set.discard(diagonal)

        board[row][col] = "."

    return result

def nQueens(n):
    board = [["."]*n for _ in range(n)]
    col = set()
    diagonal = set()
    anti_diagonal = set()
    return placeQueensOptimal(board, n, 0, col, diagonal, anti_diagonal)


if __name__ == "__main__":
    print(nQueens(4))