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
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next

                return slow.data
        return False

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
    print(sol.detectLoop(head))