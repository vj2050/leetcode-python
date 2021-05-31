# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):

        # BRUTE FORCE SOLUTION :
        # TIME COMPLEXITY : O(NlogN) since sorting
        # SPACE : O(N) new linked list creation

        nodeValues = []
        head = current = ListNode()

        for li in lists:
            while li :
                nodeValues.append(li.val)
                li = li.next
        for i in sorted(nodeValues):
            current.next = ListNode(i)
            current = current.next

        return head.next

obj = Solution()
obj.mergeKLists([[1,4,5],[1,3,4],[2,6]])