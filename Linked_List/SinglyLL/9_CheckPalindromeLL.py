class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def checkPalindrome(self, head):
        st = []
        t = head

        while t:
            st.append(t.data)
            t = t.next

        t = head
        while t:
            if st[-1] != t.data:
                return False
            st.pop()
            t = t.next

        return True

    def reverseLL(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.reverseLL(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head


    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_head = self.reverseLL(slow.next)
        first = head
        second = new_head

        while second is not None:
            if first.data != second.data:
                slow.next = self.reverseLL(new_head)
                return False
            first = first.next
            second = second.next

        slow.next = self.reverseLL(new_head)
        return True

if __name__ == "__main__":
    head = Node(3)
    second = Node(7)
    third = Node(5)
    fourth = Node(7)
    fifth = Node(3)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = None

    sol = Solution()
    print(sol.isPalindrome(head))