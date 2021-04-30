from heapq import heappush, heappop
class Solution:
    def Kth_largest(self, k, nums):
        myheap =[]
        a = 0
        for i in nums:
            heappush(myheap, i*-1)   # so that it is converted to smallest element in heap and will be at heap[0] and popped first
        for i in range(k):
            a = heappop(myheap)
        return a*-1   # to convert it back to positive

obj = Solution()
print(obj.Kth_largest(3,[3,2,1,5,6,4]))
#[-6,-5,-4,-3,-2,-1]]
# 3rd largest is num 4