from unittest.mock import right
from wsgiref.validate import header_re


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLL:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next

        t1.next = temp
        temp.prev = t1

    def removeDuplicates(self):
        if self.head is None or self.head.next is None:
            return

        temp = self.head
        t = temp.next

        while t:
            next_node = t.next

            if temp.data == t.data:
                if next_node is None:
                    temp.next = None
                else:
                    temp.next = next_node
                    next_node.prev = temp
            else:
                temp = t

            t = next_node

    def printLL(self):
        t = self.head
        while t is not None:
            print(t.data, end = " ")
            t = t.next


if __name__ == "__main__":
    sol = DoublyLL()
    sol.insert_at_end(1)
    sol.insert_at_end(1)
    sol.insert_at_end(3)
    sol.insert_at_end(3)
    sol.insert_at_end(4)
    sol.insert_at_end(5)
    sol.insert_at_end(6)
    sol.removeDuplicates()
    sol.printLL()