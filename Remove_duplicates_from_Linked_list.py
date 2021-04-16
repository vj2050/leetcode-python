class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def list2link(self, list):
        current = self.head = Node(-1)

        for i in list:
            current.next = Node(i)
            current = current.next


        return self.head.next



    def print_list(self, linkedlist):
        li = []
        current = linkedlist
        while(current is not None):
            li.append(current.val)
            current = current.next
        return li


    def removeDupes(self, linked):

        if linked is None or linked.next is None:
            return linked
        hash_set = set()
        current = linked
        hash_set.add(self.current.val)

        while(current.next is not None):
            if current.next.data in hash_set:
                current.next = current.next.next
            else:
                hash_set.add(current.next.val)
                current = current.next

        return linked





obj = MyLinkedList()
linked = obj.list2link([2,1,5,7,4])
#print(linked)
result_linked = obj.removeDupes(linked)
print(obj.print_list(result_linked))








'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def link2list(self,list):
        curr = dummy = ListNode(-1)
        for i in list:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next.val

    def removeDupes(self,linkedlist):
        






obj = Solution()
linkedlist = obj.link2list([2,1,5,7,4])
print(linkedlist)
#obj.removeDupes(linkedlist)
'''