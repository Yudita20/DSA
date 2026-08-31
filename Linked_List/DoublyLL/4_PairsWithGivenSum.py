from unittest.mock import right
from wsgiref.validate import header_re


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


    def pairsWithSum(self, target):
        if self.head is None:
            return

        set_value = set()
        result = []
        temp = self.head

        while temp:
            set_value.add(temp.data)
            temp = temp.next

        curr = self.head
        while curr:
            value = target - curr.data

            if value in set_value:
                result.append([curr.data , value])

            set_value.remove(curr.data)
            curr = curr.next

        return result

    def pairsWithTwoSum(self, target):
        if self.head is None:
            return []
        
        result = []

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        left = self.head
        right = temp

        while left != right and left.data < right.data:
            curr_sum = left.data + right.data
            if curr_sum == target:
                result.append([left.data , right.data])
                left = left.next
                right = right.prev
            elif curr_sum < target:
                left = left.next
            else:
                right = right.prev

        return result

    def printLL(self):
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next

if __name__ == "__main__":
    sol = DoublyLL()
    sol.insert_at_end(1)
    sol.insert_at_end(2)
    sol.insert_at_end(4)
    sol.insert_at_end(5)
    sol.insert_at_end(6)
    sol.insert_at_end(8)
    sol.insert_at_end(9)
    print(sol.pairsWithTwoSum(7))