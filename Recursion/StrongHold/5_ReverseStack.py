def insertAtBottom(s, curr):
    if not s:
        s.append(curr)
        return

    top = s.pop()
    insertAtBottom(s, curr)
    s.append(top)


def reverseStack(s):
    if not s:
        return

    top = s.pop()
    reverseStack(s)
    insertAtBottom(s, top)


if __name__ == "__main__":
    stack = [10,20,-5,7,15]
    reverseStack(stack)
    print(stack)
