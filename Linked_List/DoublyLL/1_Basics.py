class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class doublyLL:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t.next is not None:
            t = t.next

        t.next = temp
        temp.prev = t

    def insert_at_beg(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_at_mid(self, value, after_value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t is not None:
            if t.data == after_value:
                temp.next = t.next
                if t.next is not None:
                    t.next.prev = temp
                temp.prev = t
                t.next = temp
                return
            t = t.next

    def deletion_from_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        t = self.head
        while t.next is not None:
            t = t.next

        t.prev.next = None

    def deletion_from_beg(self):
        if self.head is None:
            return

        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def deletion_from_mid(self, value):
        if self.head is None:
            return

        t = self.head
        while t is not None:
            if t.data == value:
                if t == self.head:
                    self.deletion_from_beg()
                elif t.next is None:
                    self.deletion_from_end()
                else:
                    t.prev.next = t.next
                    t.next.prev = t.prev
                return
            t = t.next

    def printLL(self):
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next


obj = doublyLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.insert_at_end(50)
obj.insert_at_beg(5)
obj.insert_at_mid(15, 10)
obj.deletion_from_end()
obj.deletion_from_beg()
obj.deletion_from_mid(15)
obj.printLL()









