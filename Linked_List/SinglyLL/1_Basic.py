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

    def insertAtBeg(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, after_data):
        temp = Node(value)

        t = self.head
        while t.next is not None:
            if t.data == after_data:
                temp.next = t.next
                t.next = temp
                return
            t = t.next

    def deletionLL(self,value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        p = self.head
        t = self.head.next
        while t.next is not None:
            if t.data == value:
                p.next = t.next
                return
            p = t
            t = t.next
        p.next = None

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
obj.insertAtBeg(5)
obj.insertAtBeg(2)
obj.insertAtMid(7,5)
obj.deletionLL(7)
obj.printLL()



