class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def detectLoopHash(self, head):
        if head is None:
            return

        if head.next is None:
            return False

        hash_map = {}
        t = head

        while t:
            if t in hash_map:
                return True

            hash_map[t] = t.next
            t = t.next

        return False

    def detectLoopInLL(self, head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

# Driver code
if __name__ == "__main__":
    head = Node(3)
    second = Node(1)
    third = Node(7)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = None

    sol = Solution()

    if sol.detectLoopInLL(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")