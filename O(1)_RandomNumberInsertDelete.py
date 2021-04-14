import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mylist = []
        self.mydict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.mydict:
            self.mylist.append(val)
            self.mydict[val] = len(self.mylist) - 1  # key is the element, and value will be its index(calculated)
            # print(self.mydict)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val in self.mydict:  # key lookup in dict takes O(1) time
            index = self.mydict[val]
            lastvalue = self.mylist[-1]  # need to store this so that its index can be updated later in dict
            self.mylist[index], self.mylist[-1] = self.mylist[-1], self.mylist[index]  # overwriting last value in list to element to be deleted
            # update dictionary for future values
            self.mydict[lastvalue] = index
            self.mydict.pop(val)
            self.mylist.pop()
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.mylist)

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()
print(param_1, param_2,param_3,param_4,param_5,param_6,param_7)

# ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
# [[],[1],[2],[2],[],[1],[2],[]]
# Expected : [null,true,false,true,2,true,false,2]