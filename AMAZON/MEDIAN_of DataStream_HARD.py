from heapq import *
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # max heap having all other values smaller than the topmost element , low
        self.large = []  # min heap having all other values larger than the topmost element , high

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # pop from max heap and push on min heap
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[
                0]) / 2.0  # - because small == max heap storing negative numbers, inverted min heap
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()