class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def oddEven(self, head):
        if head is None:
            return

        if head.next is None or head.next.next is None:
            return head

        odd = head
        even = even_head = head.next

        while odd.next is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head

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
    new_head = sol.oddEven(head)
    sol.printLL(new_head)
