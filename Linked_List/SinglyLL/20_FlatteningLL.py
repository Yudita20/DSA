class Node:
    def __init__(self, data, next=None, child = None):
        self.data = data
        self.next = next
        self.child = child


class Solution:
    def mergeLL(self, h1, h2):
        dummy_Node = Node(-1)
        res = dummy_Node

        while h1 is not None and h2 is not None:
            if h1.data < h2.data:
                res.child = h1
                res = h1
                h1 = h1.child
            else:
                res.child = h2
                res = h2
                h2 = h2.child
            res.next = None

        if h1:
            res.child = h1
        else:
            res.child = h2

        if dummy_Node.child:
            dummy_Node.child.next = None

        return dummy_Node.child

    def flattenLL(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.flattenLL(head.next)

        merged_head = self.mergeLL(head, new_head)
        return merged_head


    def printLL(self, head):
        while head is not None:
            print(head.data, end=" ")
            head = head.child


if __name__ == "__main__":
    head = Node(5)
    head.child = Node(14)

    head.next = Node(10)
    head.next.child = Node(14)

    head.next.next = Node(12)
    head.next.next.child = Node(20)
    head.next.next.child.child = Node(23)

    head.next.next.next = Node(7)
    head.next.next.next.child = Node(17)

    sol = Solution()
    new_head = sol.flattenLL(head)
    sol.printLL(new_head)





