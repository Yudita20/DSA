class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def intersectP(self, head1, head2):
        temp1  = head1
        temp2 = head2
        seen = set()

        while temp1:
            seen.add(temp1)
            temp1 = temp1.next

        while temp2:
            if temp2 in seen:
                return temp2.data
            temp2 = temp2.next

        return None

    def intersectPresent(self, head1, head2):
        t1 , t2 = head1 , head2

        while t1 != t2:
            t1 = head2 if t1 is None else t1.next
            t2 = head1 if t2 is None else t2.next

        return t1.data

if __name__ == "__main__":
    # List A
    headA = Node(1)
    s = Node(2)
    t = Node(3)
    f = Node(4)

    headA.next = s
    s.next = t
    t.next = f
    f.next = None

    # List B
    headB = Node(5)
    second = Node(3)
    third = Node(4)

    headB.next = t
    second.next = f
    third.next = None

    sol = Solution()
    print(sol.intersectP(headA, headB))
    print(sol.intersectPresent(headA, headB))


