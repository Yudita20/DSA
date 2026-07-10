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

        prev_node = None
        curr = self.head

        while curr is not None:
            prev_node = curr.prev
            curr.prev , curr.next = curr.next , curr.prev
            curr = curr.prev

        self.head = prev_node.prev
        return self.head

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
obj.reverse_DLL()
obj.printLL()