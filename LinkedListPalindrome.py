class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def palindromeCheck(self, mylist):
        result = []
        current = mylist
        while(current is not None):
            result.append(current.val)
            current = current.next
        return result == result[::-1]

    def displaylist(self):
        current = self.head
        li = []
        while(current!=None):
            li.append(current.val)
            current = current.next

        print(li)

    def add_at_tail(self,val):
        mynewNode = ListNode(val)
        #print(mynewNode.val)
        current = self.head
        if current==None:
            self.head = mynewNode
            print("head is only the newnode")
        else:
            while(current.next!=None):
                #print("curr ", current.val)
                current = current.next
            current.next = mynewNode
        return self.head


obj = MyLinkedList()
t1= obj.add_at_tail(1)
t2= obj.add_at_tail(2)
t3= obj.add_at_tail(2)
t4= obj.add_at_tail(1)
obj.displaylist()
result = obj.palindromeCheck(t4)
print(result)

