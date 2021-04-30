# need another class for bucket to hold all the values to avoid collision, can use array here/ linkedlist

class MyBucket:  # parent class
    def __init__(self):
        self.bucket = []

    def getval_fromBucket(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update_inBucket(self, key, value):
        foundkey = False

        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                foundkey = True
                break

        if not foundkey:
            self.bucket.append((key, value))

    def remove_fromBucket(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap:  # child class

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069  # prime number as base of modulo, to avoid collisions
        self.hash_table = [MyBucket() for i in
                           range(self.key_space)]  # for every key, have a bucket storing multiple values

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # always first find hashed_key and then pass it to bucket
        hash_key = key % self.key_space
        self.hash_table[hash_key].update_inBucket(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].getval_fromBucket(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove_fromBucket(key)


#Your MyHashMap object will be instantiated and called as such:
# ["MyHashMap","put","put","get","get","put","get","remove","get"]
# [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
param_2 = obj.get(1)
obj.remove(1)