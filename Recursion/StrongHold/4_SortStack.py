def insertElement(s, curr):
    if not s or s[-1] <= curr:
        s.append(curr)
        return

    top = s.pop()
    insertElement(s, curr)
    s.append(top)


def sortStack(s):
    if not s:
        return

    top_element = s.pop()
    sortStack(s)
    insertElement(s, top_element)


if __name__ == "__main__":
    stack = [4,1,3,2]
    sortStack(stack)
    print(stack)


