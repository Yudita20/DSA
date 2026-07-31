class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLL:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next

        t1.next = temp

    def middle_of_list_brute(self):
        # Empty linked list
        if self.head is None:
            return

        # Single node present in Linked list
        if self.head.next is None:
            return self.head.data

        t = self.head
        count_len = 0

        while t is not None:
            count_len += 1
            t = t.next

        t = self.head
        c = 0
        while c != count_len//2:
            c += 1
            t = t.next

        return t.data

    def middle_of_list(self):
        # Slow and fast Pointer
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

# Similar problems
# First middle in even length linked list
    def mol(self):
        # Empty linked list
        if self.head is None:
            return

        # Single node present in Linked list
        if self.head.next is None:
            return self.head.data

        # Slow and fast Pointer
        slow = self.head
        fast = self.head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data


obj = SinglyLL()
obj.insert_at_end(3)
obj.insert_at_end(8)
obj.insert_at_end(2)
obj.insert_at_end(1)
print(obj.middle_of_list_brute())
print(obj.middle_of_list())
print(obj.mol())
