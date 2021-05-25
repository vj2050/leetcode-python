# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = head
        size = 0
        # while loop to find out length of list
        while (current is not None):
            # print(current.val)
            size += 1
            current = current.next
        print("length", size)
        # EDGE Cases :
        if size == 1:  # if only one node, delete that node and return []
            head = None
            return head

        size = size - n
        if size == 0:
            return head.next

        current2 = dummy
        while (size > 0):
            size -= 1
            current2 = current2.next
        print(current2.val, size)
        current2.next = current2.next.next
        return head


        '''
        temp = head

        numnodes = 0
        while(temp is not None):
            temp = temp.next
            numnodes+=1

        K = numnodes - n

        prev = None
        ptr = head
        while(K!=0):
            prev = ptr
            ptr = ptr.next
            K -=1


        if prev is None:
            return head.next

        else:
            prev.next = ptr.next
            ptr.next = None
            return head
        '''

