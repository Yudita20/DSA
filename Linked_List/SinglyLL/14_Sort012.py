class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def sortLL012(self, head):
        zero_dummy = Node(-1)
        one_dummy = Node(-1)
        two_dummy = Node(-1)

        zero , one, two = zero_dummy, one_dummy, two_dummy

        curr = head

        while curr:
            next_node = curr.next
            curr.next = None
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = next_node

        zero.next = one_dummy.next if one_dummy.next else two_dummy.next
        one.next = two_dummy.next
        two.next = None

        return zero_dummy.next

    def printLL(self, head):
        if head is None:
            print("Linked list is empty")
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    head = Node(2)
    second = Node(1)
    third = Node(2)
    fourth = Node(1)
    # fifth = Node(2)
    # sixth = Node(0)
    # seventh = Node(0)

    head.next = second
    second.next = third
    third.next = fourth
    # fourth.next = fifth
    # fifth.next = sixth
    # sixth.next = seventh
    # seventh.next = None
    fourth.next = None

    sol = Solution()
    new_head = sol.sortLL012(head)
    sol.printLL(new_head)


