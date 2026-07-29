class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLL:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t.next is not None:
            t = t.next

        t.next = temp
        temp.prev = t

    def insertAtBeg(self,value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMid(self, value, after_data):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t is not None:
            if t.data == after_data:
                temp.next = t.next
                if t.next is not None:
                    t.next.prev = temp
                temp.prev = t
                t.next = temp
                return
            t = t.next

    def deletionLL(self, value):
        if self.head is None:
            return

        # Deletion from starting
        if self.head.data == value:
            self.head = self.head.next
            return

        t = self.head
        while t.next is not None:
            # deletion from mid
            if t.data == value:
                t.prev = t.next
                return
            t = t.next

        # Deletion from end
        t.prev.next = None

    def printLL(self):
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next

obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
obj.insertAtBeg(5)
obj.insertAtBeg(2)
obj.insertAtMid(15, 10)
obj.deletionLL(50)
obj.printLL()










