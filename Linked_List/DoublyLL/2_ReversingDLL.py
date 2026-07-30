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
        if self.head is None:
            return

        if self.head.next is None:
            return self.head

        p = None
        curr = self.head

        while curr is not None:
            curr.prev, curr.next = curr.next, curr.prev
            p= curr
            curr = curr.prev

        self.head = p
        return self.head.data

    def printLL(self):
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next

obj = DoublyLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.insert_at_end(50)
obj.insert_at_end(55)
obj.insert_at_end(57)
print(obj.reverse_DLL())
print("Reversed List:")
obj.printLL()