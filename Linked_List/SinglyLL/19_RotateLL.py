class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def listLength(self, head):
        temp = head
        l = 1
        while temp.next is not None:
            temp = temp.next
            l += 1

        return l

    def rotateLL(self, head, k):
        if head is None or head.next is None:
            return head

        # Find length of the list
        length_list = self.listLength(head)

        #How many times the list needs to Rotate
        rotate_right = k % length_list
        if rotate_right == 0:
            return head

        split = length_list - rotate_right

        dummy = Node(-1)
        dummy.next = head

        slow = dummy

        for _ in range(split):
            slow = slow.next

        new_link = slow.next
        slow.next = None

        curr = new_link

        while curr.next is not None:
            curr = curr.next

        curr.next = dummy.next

        return new_link

    def printLL(self, head):
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = None

    sol = Solution()
    new_head = sol.rotateLL(head, 3)
    sol.printLL(new_head)



