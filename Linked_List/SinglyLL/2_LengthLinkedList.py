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

    def length_of_linked_list(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next

        return count

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next

obj = SinglyLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
print(obj.length_of_linked_list())
# obj.printLL()