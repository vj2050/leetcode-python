# Definition for singly-linked list.  ;;;;;; Example of inheritance as Listnode class's attributes are used in Solution class
class ListNode:                                 #NODE class
    def __init__(self, val=0, next=None):       # Function to initialize Node object
        self.val = val
        self.next = next

# SOLUTION class contains a Node object
class Solution:
    # def __init__(self):                     # Optional : Function to initialize linkedlist (Here "Solution") class; to initialize head
    #     self.head = None

    def list2link(self, list1, list2):         # function to create linked list from a normal list passed.
        cur1 = dummy1 = ListNode(-1)
        cur2 = dummy2 = ListNode(-1)
        for i in (list1):
            cur1.next = ListNode(i)
            cur1 = cur1.next
        for j in (list2):
            cur2.next = ListNode(j)
            cur2 = cur2.next
        return dummy1.next, dummy2.next


    def mergeInBetween(self, list1, a,b,list2):

        start, end = None, list1
        print()
        for i in range(b):  # node initially pointing at 0th node
            if i == a - 1:
                start = end  # end is 2 here up to now before incrementing hence start is also 2 now
                print("ffffffffffff")
            end = end.next
        print(end.val)  # at node val 4 here

        print("start", start.val)
        print("end", end.val)

        start.next = list2

        while list2.next != None:
            list2 = list2.next
        # here i will reach the last node of list 2. I need to connect that with list1 remaining nodes

        if list2.next == None:
            list2.next = end.next  # 4-->next  == 5
        ##### In order to print out the resulting merged linked list, TRAVERSE THROUGH EACH NODE AND PRINT.
        tempfinal = list1
        while tempfinal!=None:
            print(tempfinal.val)
            tempfinal = tempfinal.next

        #return list1

obj = Solution()
list1, list2= obj.list2link([0,1,2,3,4,5],[1000000,1000001,1000002])
#result =
obj.mergeInBetween(list1,3,4,list2)

