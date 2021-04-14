class ABC:

    def __init__(self,value=None):
        self.val=value
        self.next=None

class XYZ:

    def __init__(self):
        self.head=ABC()

    def appendfunc(self,value):
        newnode=ABC(value)
        current=self.head

        while(current.next!=None):
            current=current.next

        current.next=newnode

    def display(self):
        li=[]
        current=self.head
        while(current.next!=None):
            current=current.next
            li.append(current.val)
        print(li)



    def addnode(self,value,index):
        newnode=ABC(value)
        current=self.head

        for i in range(index+1):
            current=current.next

        newnode.next=current.next
        current.next=newnode

    def count(self):
        current=self.head
        cnnt=0

        while(current.next!=None):
            current=current.next
            cnnt=cnnt+1
        #print(cnnt)
        return cnnt

    def value(self,index):
        current=self.head
        if index>self.count():
            print("List index out of range")
            return 0
        else:
            for i in range(index+1):
                current=current.next
            print(current.val)

    def deletenode(self,index):
        current=self.head

        for i in range(index):
            current=current.next
        current.next=current.next.next

obj=XYZ()
obj.appendfunc(4)
obj.appendfunc(2)
obj.appendfunc(5)
obj.appendfunc(1)
obj.display()
obj.addnode(9,2)
obj.display()
print(obj.count())
obj.value(3)
obj.deletenode(3)
obj.display()