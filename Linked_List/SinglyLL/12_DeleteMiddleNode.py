class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:

    def deleteMiddleNode(self, head):
        if head is None or head.next is None:
            return None

        dummy = Node(0, head)
        slow = dummy
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy.next

    def printLL(self, head):
        if head is None:
            print("Linked list is empty")
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = None

    sol = Solution()
    new_head = sol.deleteMiddleNode(head)
    sol.printLL(new_head)
