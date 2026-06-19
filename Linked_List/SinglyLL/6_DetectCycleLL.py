class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def detectLoop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def detectLoopBrute(self , head):
        hash_map = {}

        t = head
        while t:
            if t in hash_map:
                return True

            hash_map[t] = t.next
            t = t.next
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
    third.next = head
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    sol = Solution()

    if sol.detectLoopBrute(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")