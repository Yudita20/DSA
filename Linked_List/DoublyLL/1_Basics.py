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

    def insert_at_beg(self,value):
        temp =Node(value)
        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    # Inserting after the key
    def insert_at_mid(self,value,key):
        temp = Node(value)
        t1 = self.head

        while t1 is not None:
            if t1.data == key:
                break
            else:
                t1 = t1.next
        temp.next = t1.next
        t1.next.prev = temp
        temp.prev = t1
        t1.next = temp

    def deletionDll(self,value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            #Head is the node to be deleted
            self.head = self.head.next
            self.head.prev = None
            return

        t = self.head
        while t is not None:
            # Last Node
            if t.next is None:
                if t.data == value:
                    t.prev.next = None
                return

            # Middle Node
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next



    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next

obj = DoublyLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_beg(5)
obj.insert_at_mid(15,10)
obj.printLL()


