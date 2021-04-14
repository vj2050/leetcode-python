
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.size = 0

    def create(self,value):
        myNewnode = Node(value)

        current = self.head
        if current is None:
            self.head = myNewnode
        else:
            while current.next is not None:
                current = current.next
            current.next = myNewnode

        self.size +=1
        return self.head


    def display(self):
        current = self.head
        li = []
        while(current is not None):
            li.append(current.val)
            current = current.next
        return li

    def detectCycle(self, head, pos):
        visited_node = set()

        current = self.head
        tail = self.head
        i=0
        while(tail.next is not None):
            tail = tail.next

        while(i<pos-1 and current is not None):
            current = current.next
            i+=1

        print("current is ", current.val)
        tail.next = current.next
        print("now ", tail.next.val)

        while head is not None:
            if head.val in visited_node:
                return head.val
            else:
                visited_node.add(head.val)
                head = head.next
        return


obj = Solution()
obj.create(2)
obj.create(1)
obj.create(4)
obj.create(3)
head = obj.display()
obj.detectCycle(head, 1)
print(obj.display())