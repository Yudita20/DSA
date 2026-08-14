class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def mergeTwoList(self, left, right):
        dummy = Node(-1)
        curr = dummy

        while left is not None and right is not None:
            if left.data <= right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        if left:
            curr.next = left
        else:
            curr.next = right

        return dummy.next

    def middleLL(self, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortLL(self, head):
        if head is None or head.next is None:
            return head

        middle = self.middleLL(head)

        right = middle.next
        middle.next = None

        left = self.sortLL(head)
        right = self.sortLL(right)

        return self.mergeTwoList(left, right)

    def printLL(self, head):
        if head is None:
            print("Linked list is empty")
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    head = Node(1)
    second = Node(3)
    third = Node(6)
    fourth = Node(8)
    fifth = Node(4)
    sixth = Node(2)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = None

    sol = Solution()
    new_head = sol.sortLL(head)
    sol.printLL(new_head)

