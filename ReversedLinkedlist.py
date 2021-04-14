### Video Reference : https://www.youtube.com/watch?v=XDO6I8jxHtA

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
        return dummy
    def reverseList(self, head):
        # Instead of reversing the values of each node, simply Reverse the pointers of each node entirely.
        prev = None
        while (head):
            temp = head  # None(prev)   head+temp
            head = head.next  # None(prev)   temp-->head
            temp.next = prev  # prev <-- temp   head    reversed the pointer
            prev = temp  # <-- temp+prev

        #return prev
        # Now pointing at the actual head of the node; here not returning temp because when Head becomes None, and doesnt enter while loop at all, and when tries to return Temp, then throws not defined temp error
        tempfinal = prev
        while(tempfinal.val!=-1):    #since we took -1 as dummy initial node
            print(tempfinal.val)
            tempfinal = tempfinal.next

obj = Solution()
list = obj.link2list([1,2,3,4,5])
obj.reverseList(list)