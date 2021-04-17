# Given SORTED Linked list, remove ALL duplicates and return head of SORTED linked list:
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def list2link(self, list):
        current = self.head = Node(-1)   # dUMMY NODE ALWAYS
        for i in list:
            current.next = Node(i)
            current = current.next
        return self.head     #.next

    def print_list(self, linkedlist):
        li = []
        current = linkedlist.next    # for printing purposes, avoided -1
        while(current is not None):
            li.append(current.val)
            current = current.next
        return li

    def removeDupes(self, linked):
        prev = linked     # already pointing at DUMMY NODE -1
        head= linked.next     #local head
        # prev pointer will always be one step behind head
        #print("head val ", head.val, prev.val)

        while (head is not None):  # head starts from actual linked list, here 1
            if head.next and head.val == head.next.val:  # dupes start
              while (head.next and head.val == head.next.val):
                    head = head.next

                # after while loop we come at last unique element from dupes, eg: 0,1,1,1,2,3 ,... head pointing at last 1
              prev.next = head.next  # removing all dupes prev was pointing at predecessor i.e 0 -> 2.......4

            else:
                prev = prev.next  # increment previous pointer

            head = head.next  # 2,3
        return linked  # since predecessor is pointing at dummy node 0

obj = MyLinkedList()
linked = obj.list2link([1,2,3,3,4,4,5])
print(obj.print_list(linked))
#print(linked)
result_linked = obj.removeDupes(linked)
print(obj.print_list(result_linked))






