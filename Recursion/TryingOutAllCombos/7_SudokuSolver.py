# def isValid(board, row, col, value):
#     for i in range(9):
#
#         # Check column
#         if board[i][col] == value:
#             return False
#
#         # Check row
#         if board[row][i] == value:
#             return False
#
#         # Check 3x3 box
#         start_i = row // 3 * 3
#         start_j = col // 3 * 3
#
#         for k in range(0, 3):
#             for l in range(0, 3):
#                 if board[start_i + k][start_j + l] == value:
#                     return False
#
#     return True
#
#
# def sudokuSolver(board):
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == ".":
#                 for k in range(1, 10):
#                     if isValid(board, i, j, str(k)):
#
#                         board[i][j] = str(k)
#
#                         if sudokuSolver(board):
#                             return True
#
#                         board[i][j] = "."
#
#                 return False
#
#     return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []


    for r in range(9):
        for c in range(9):

            value = board[r][c]

            if value != ".":

                box = (r // 3) * 3 + (c // 3)

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

            else:
                empties.append((r,c))


    def backTrack(idx):
        if idx == len(empties):
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    box = (i // 3) * 3 + (j // 3)

                    for value in "123456789":

                        if value not in rows[i] and value not in cols[j] and value not in boxes[box]:

                            board[i][j] = value
                            rows[i].add(value)
                            cols[j].add(value)
                            boxes[box].add(value)

                            if backTrack(idx + 1):
                                return True

                            board[i][j] = "."
                            rows[i].remove(value)
                            cols[j].remove(value)
                            boxes[box].remove(value)

                    return False

    backTrack(0)
    print(board)
