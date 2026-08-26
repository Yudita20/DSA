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


    def delOccurrence(self, target):
        if self.head is None:
            return

        while self.head is not None and self.head.data == target:
            self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        temp = self.head
        while temp:
            next_node = temp.next
            if temp.data == target:
                if temp.next is None:
                    temp.prev.next = None
                else:
                    temp.prev.next = next_node
                    next_node.prev = temp.prev
            temp = next_node


    def printLL(self):
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next

if __name__ == "__main__":
    sol = DoublyLL()
    sol.insert_at_end(1)
    sol.insert_at_end(2)
    sol.insert_at_end(3)
    sol.insert_at_end(1)
    sol.insert_at_end(4)
    sol.insert_at_end(1)
    sol.delOccurrence(1)
    sol.printLL()