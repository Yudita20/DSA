def ratInMaze(box, grid_dim, i, j, curr_st = "" , result = None):
    if result is None:
        result = []

    if i < 0 or j < 0 or i >= grid_dim or j >= grid_dim or box[i][j] != 1:
        return False

    if i == grid_dim-1 and j == grid_dim-1:
        result.append(curr_st)
        return result

    box[i][j] = "$"

    curr_st += "D"
    ratInMaze(box, grid_dim, i + 1, j, curr_st, result)
    curr_st = curr_st[0: len(curr_st) - 1]

    curr_st += "L"
    ratInMaze(box, grid_dim, i, j - 1, curr_st, result)
    curr_st = curr_st[0: len(curr_st) - 1]

    curr_st += "R"
    ratInMaze(box, grid_dim, i, j + 1, curr_st, result)
    curr_st = curr_st[0: len(curr_st) - 1]

    curr_st += "U"
    ratInMaze(box, grid_dim, i - 1, j, curr_st, result)
    curr_st = curr_st[0: len(curr_st) - 1]

    box[i][j] = 1

    return result


if __name__ == "__main__":
    grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
    n = 4
    if grid[0][0] != 0:
        print(ratInMaze(grid, n, 0, 0))
    else:
        print(-1)
