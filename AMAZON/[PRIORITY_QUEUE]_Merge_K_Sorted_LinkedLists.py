# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = current = ListNode()

        q = PriorityQueue()

        for l in lists:
            # append only head's value + pointer as tuple of each of the lists into queue and take min out of them
            if l is not None:
                q.put((l.val, l))

        while not q.empty():
            value, nodePointer = q.get()  # extract the min tuple
            current.next = ListNode(value)  # add this node to resultant linked list
            current = current.next
            nodePointer = nodePointer.next  # the element selected from ith list, increment its pointer and look ahead
            if nodePointer is not None:
                q.put((nodePointer.val, nodePointer))

        return head.next

















