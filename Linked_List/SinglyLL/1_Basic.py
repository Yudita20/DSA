class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLL:
    def __init__(self, head=None):
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


    def insert_at_beg(self , value):
        temp = Node(value)

        # inserting when list is empty
        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head = temp

    def insert_at_mid(self,value,after_data_value):
        temp = Node(value)
        t = self.head

        while t is not None:
            if t.data == after_data_value:
                temp.next = t.next
                t.next = temp
                return

            t = t.next

    def delete_from_beg(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        t1 = self.head
        prev = t1
        while t1.next is not None:
            prev = t1
            t1 = t1.next

        prev.next = None

    def delete_from_mid(self , data):
        if self.head is None:
            return

        t1 = self.head
        prev = t1
        if data == self.head.data:
            self.head = self.head.next
            return

        while t1.next is not None:
            if t1.data == data:
                prev.next = t1.next
                return
            prev = t1
            t1 = t1.next

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data , end =" ")
            t1 = t1.next

obj = SinglyLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_beg(5)
obj.insert_at_mid(15,10)
obj.delete_from_beg()
obj.delete_from_end()
obj.delete_from_mid(15)
obj.printLL()




