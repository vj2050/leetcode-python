# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = current = ListNode()  # resultant empty linked list
        q = []

        for l in lists:
            # append only head's value + pointer as tuple of each of the lists into queue and take min out of them
            if l is not None:
                heappush(q, (l.val, l))

        while q:
            value, nodePointer = heappop(q)  # extract the min tuple
            # print("value , pointer ", value, nodePointer)
            current.next = ListNode(value)  # add this node to resultant linked list
            current = current.next
            nodePointer = nodePointer.next  # element selected from ith list,increment its pointer and look ahead
            if nodePointer is not None:
                heappush(q, (nodePointer.val, nodePointer))

        return head.next

















