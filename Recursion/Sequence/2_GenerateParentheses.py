def checkValidity(s):
    count = 0
    for ch in s:
        if ch == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return None

    if count == 0:
        return s
    else:
        return None

def generateParenthesesBrute(n, curr_string="", result = None):
    if result is None:
        result = []

    if len(curr_string) == n * 2:
        well_formed_string = checkValidity(curr_string)
        if well_formed_string is not None:
            result.append(curr_string)
        return

    generateParenthesesBrute(n, curr_string + "(", result)
    generateParenthesesBrute(n, curr_string + ")", result)

    return result

def generateParentheses(n, curr_string = "", result = None, open_bracket = 0, close_bracket = 0):
    if result is None:
        result = None

    if len(curr_string) == n * 2:
        result.append(curr_string)
        return

    if open_bracket < n:
        generateParentheses(n, curr_string + "(", result, open_bracket + 1, close_bracket)

    if close_bracket < open_bracket:
        generateParentheses(n, curr_string + ")", result, open_bracket, close_bracket + 1)

    return result

if __name__ == "__main__":
    print(generateParenthesesBrute(3))
    print(generateParentheses(1))
