class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [0] * k
        self.capacity = k
        self.count = 0  # current size of queue
        self.headIndex = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count == self.capacity:  # if queuefull, return
            return False
        else:
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.count == 0 or self.capacity == 0:
            return False
        else:
            self.headIndex = (self.headIndex + 1) % self.capacity  # FIFO
            self.count -= 1
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        print(self.queue)
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.count == self.capacity:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()