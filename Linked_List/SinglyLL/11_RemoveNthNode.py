class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def lengthOfLL(self, head):
        if head is None:
            return 0

        if head.next is None:
            return 1

        temp = head
        linked_len = 0
        while temp:
            linked_len += 1
            temp = temp.next

        return linked_len

    def removeNthNode(self, head, n):
        if head is None:
            return head

        list_len = self.lengthOfLL(head)
        idx = list_len - n + 1

        if idx == 1:
            head = head.next
            return head

        t = head
        p = None
        count = 1
        while count != idx:
            count += 1
            p = t
            t = t.next

        p.next = t.next
        return head


    def removeNthNodeOptimal(self, head, n):
        dummy = Node(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

    def printLL(self, head):
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
    new_head = sol.removeNthNodeOptimal(head,3)
    sol.printLL(new_head)
