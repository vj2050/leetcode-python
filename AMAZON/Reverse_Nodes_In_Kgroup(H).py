# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helperReverse(self, head, k):  # for reversing k set of nodes
        newHead = None
        currentPtr = head
        while (k):
            nextNode = currentPtr.next  # 2
            currentPtr.next = newHead
            # update newHead
            newHead = currentPtr
            # move to the next node
            currentPtr = nextNode
            k -= 1
        return newHead

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        count = 0
        ptr = head  # head is already pointing at 1st node in list initially
        while (count < k and ptr is not None):
            ptr = ptr.next
            count += 1
        # only for verification purposes :
        if count == k:
            # verified that k nodes set present in list, reverse them and get reverse lists' head
            reverseHead = self.helperReverse(head, k)

            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reverseHead
        return head


