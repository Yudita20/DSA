class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def reverseLL(self, head):
        if head is None:
            return

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

    def getkthNode(self, curr, k):
        k -= 1
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr

    def reverseInKSize(self, head, k):
        temp = head
        prevLast = None

        while temp:
            kth = self.getkthNode(temp, k)
            if kth is None:
                if prevLast:
                    prevLast.next = temp
                break

            next_node = kth.next
            kth.next = None
            self.reverseLL(temp)

            if temp == head:
                head = kth
            else:
                prevLast.next = kth

            prevLast = temp
            temp = next_node

        return head

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
   new_head = sol.reverseInKSize(head, 2)
   sol.printLL(new_head)





