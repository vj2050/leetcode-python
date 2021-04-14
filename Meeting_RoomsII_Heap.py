import heapq  # priority queue. Each time the smallest of heap element is popped(min heap).
# Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element also returns the smallest element each time.

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        myheap = [intervals[0][1]]     # heap to store endtimes only.
        if intervals == []:
            return 0

        for start, end in intervals[1:]:
            if myheap[0] <= start:
                heapq.heappop(myheap)  # always reorders itself and min(heap) is popped
            heapq.heappush(myheap, end)
        return len(myheap)

myobj = Solution()
result = myobj.minMeetingRooms([[9,10],[4,9],[4,17]])
print("Number of meeting rooms required are=> ", result)




