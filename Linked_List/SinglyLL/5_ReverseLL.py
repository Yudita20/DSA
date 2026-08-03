class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SinglyLL:
    def __init__(self , head=None):
        self.head = head

    def insertAtEnd(self,value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t.next is not None:
            t = t.next

        t.next = temp

    def reverseLL(self):
        if self.head is None:
            return

        if self.head.next is None:
            return self.head

        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # Reverse the list using recursion
    def reverseRecursion(self):
        self.head = self._reverse(self.head)

    def _reverse(self, head):
        if head is None or head.next is None:
            return head

        new_head = self._reverse(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head

    # Print list in reverse order
    def printListRecursion(self):
        self._printReverse(self.head)

    def _printReverse(self, head):
        if head is None:
            return
        self._printReverse(head.next)
        print(head.data)

    # Count number of nodes using recursion
    def countNodes(self):
        return self._count(self.head)

    def _count(self, head):
        if head is None:
            return 0
        return 1 + self._count(head.next)

    # Search nodes using recursion
    def searchNodes(self, target):
        return self._search(self.head, target)

    def _search(self, head, target):
        if head is None:
            return False

        if head.data == target:
            return True

        return self._search(head.next, target)

    # Print the linked list
    def printLL(self):
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next


obj = SinglyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
# obj.reverseLL()
obj.reverseRecursion()
obj.printLL()





