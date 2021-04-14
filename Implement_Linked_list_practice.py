class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

########### ALWAYS assign Head and size as NONE adn 0 respectively first *******
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_at_head(self,value):
        mynewNode = Node(value)
        mynewNode.next = self.head
        self.head = mynewNode
        print("added at head", self.head.val)
        self.size +=1

    def add_at_tail(self,val):
        mynewNode = Node(val)
        print(mynewNode.val)
        current = self.head

        if current==None:
            self.head = mynewNode
            print("head is only the newnode")
        else:
            while(current.next!=None):
                print("curr ", current.val)
                current = current.next

            current.next = mynewNode
        self.size+=1

        #print("added ",current.val )

    def displaylist(self):
        current = self.head
        li = []
        while(current!=None):
            li.append(current.val)
            current = current.next

        print(li)

    def getvalue_at_index(self, index):
        current = self.head
        if current is None:
            return -1
        else:
            i=0
            while(i<index and current is not None):
                current = current.next
                i+=1
            # current already reached dedicated index even if i reached index - 1 location
            return current.val

    def add_at_index(self, index, value):     # we have to add node before the iTH index
        mynewNode = Node(value)
        current = self.head

        if index < 0 or index > self.size:
            return
        if index ==0:
            self.add_at_head(value)
        else:
            i=0
            while(i< index-1 and current is not None):
                #print(i)
                #print("printing current.val ", current.val)
                current = current.next
                i+=1
            mynewNode.next = current.next
            current.next = mynewNode
            self.size+=1


    def delete_at_index(self,index):   #we have to delete ith index node
        current = self.head
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.head = current.next

        else:
            i = 0
            while(i<index-1 and current is not None):
                current = current.next
                i+=1
                #current = 5

            current.next = current.next.next

        self.size -=1

obj = MyLinkedList()
obj.add_at_head(1)
obj.add_at_head(2)
obj.displaylist()
obj.add_at_tail(3)
obj.add_at_tail(4)
obj.displaylist()
obj.add_at_index(2,5)
obj.displaylist()
value = obj.getvalue_at_index(2)
obj.delete_at_index(2)
obj.displaylist()
print(value)
