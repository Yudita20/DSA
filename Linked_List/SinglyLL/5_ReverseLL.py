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
obj.reverseLL()
obj.printLL()





