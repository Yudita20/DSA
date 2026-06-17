class Node:
    def __init__(self , data , prev=None , next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLL:
    def __init__(self,head=None):
        self.head = head

    def insert_at_end(self,value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next

        t1.next = temp
        temp.prev = t1


    def reverse_DLL(self):
        t = self.head

        while t is not None:
           if t.next is None:
               break
           t = t.next

        first = self.head
        last = t

        while first != last and first.prev != last:
            first.data , last.data = last.data , first.data
            first = first.next
            last = last.prev

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = DoublyLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.insert_at_end(50)
obj.reverse_DLL()
obj.printLL()