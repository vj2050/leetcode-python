from heapq import heappush, heappop, heapify
class Solution:
    def Kth_smallest(self, k, nums):
        myheap =[]
        a = 0
        for i in nums:
            heappush(myheap, i)
        for i in range(k):
            a = heappop(myheap)
        return a




obj = Solution()
print(obj.Kth_smallest(3,[3,2,1,5,6,4]))
#[1,2,3,4,5,6]
# 3rd smallest is num 3