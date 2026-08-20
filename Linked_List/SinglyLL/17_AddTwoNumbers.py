class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def addTwo(self, list_a, list_b):
        dummy = Node(-1)
        temp = dummy
        carry = 0

        while (list_a is not None or list_b is not None) or carry:
            sum_value = 0

            if list_a is not None:
                sum_value += list_a.data
                list_a = list_a.next

            if list_b is not None:
                sum_value += list_b.data
                list_b = list_b.next

            sum_value += carry

            carry = sum_value // 10
            new_node = Node(sum_value%10)
            temp.next = new_node
            temp = temp.next

        return dummy.next

    def printLL(self, head):
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    headA = Node(4)
    second = Node(5)
    third = Node(6)

    headA.next = second
    second.next = third
    third.next = None

    headB = Node(1)
    s = Node(2)
    t = Node(3)

    headB.next = s
    s.next = t
    t.next = None

    sol = Solution()
    new_head = sol.addTwo(headA, headB)
    sol.printLL(new_head)




