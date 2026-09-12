def generateBS(n, curr_string = "", result=None):
    if result is None:
        result = []

    if len(curr_string) == n:
        result.append(curr_string)
        return

    generateBS(n, curr_string+"0",result)

    if not curr_string or curr_string[-1] != "1":
        generateBS(n , curr_string+"1" , result)

    return result

if __name__ == "__main__":
    print(generateBS(3))

