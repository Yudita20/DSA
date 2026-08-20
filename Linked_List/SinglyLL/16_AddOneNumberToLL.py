class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def insertAtBeg(self, head, value):
        if head is None:
            return

        temp = Node(value)
        temp.next = head
        head = temp
        return head


    def addOne(self, node):
        if node is None:
            return 1

        carry = self.addOne(node.next)
        total = node.data + carry
        node.data = total % 10
        carry = total // 10
        return carry

    def oneAddHead(self, head):
        carry = self.addOne(head)

        if carry:
            return self.insertAtBeg(head, carry)
        return head


    def printLL(self, head):
        if head is None:
            print("Linked list is empty")
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    head = Node(9)
    second = Node(9)

    head.next = second
    second.next = None

    sol = Solution()
    new_head = sol.oneAddHead(head)
    sol.printLL(new_head)


