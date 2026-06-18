class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLL:
    def __init__(self,head=None):
        self.head = head

    def insert_at_end(self , value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next

        t1.next = temp

    def reverseLL(self):
        temp = self.head
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev.data

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next

obj = SinglyLL()
obj.insert_at_end(3)
obj.insert_at_end(8)
obj.insert_at_end(7)
obj.insert_at_end(1)
obj.insert_at_end(3)
print(obj.reverseLL())
