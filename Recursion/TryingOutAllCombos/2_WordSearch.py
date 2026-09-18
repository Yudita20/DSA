def findWord(matrix, word, i, j, idx = 0):
    if idx == len(word):
        return True

    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != word[idx]:
        return False

    temp = matrix[i][j]
    matrix[i][j] = "$"

    found = findWord(matrix, word, i + 1, j, idx + 1) or findWord(matrix, word, i - 1, j, idx + 1) or findWord(matrix, word, i, j + 1, idx + 1) or findWord(matrix, word, i, j - 1, idx + 1)

    matrix[i][j] = temp

    return found


def wordSearch(matrix, word):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if board[i][j] == word[0] and findWord(matrix, word, i , j, 0):
                return True

    return False



if __name__ == "__main__":
    board = [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ]
    words = "EAT"
    print(wordSearch(board, words))

