class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = collections.OrderedDict()
        # print(self.cache)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            value = self.cache[key]
            del self.cache[key]
            # print(self.cache)
            self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value  # update with new "value" OR simply Insert the new fresh value

        if len(self.cache) > self.size:
            self.cache.popitem(
                last=False)  # popitem() is used to pop last topmost item inserted in dictionary ; by default pops in LIFO fashion. Hence last= False will pop in FIFO order. Hence least used item is popped in FIFO manner

# Your LRUCache object will be instantiated and called as such:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)


