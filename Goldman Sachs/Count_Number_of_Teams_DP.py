# defaultdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
# Time Complexity : O(N^2)
from collections import defaultdict

class Solution:
    def numTeams(self, rating) :
        lesser = defaultdict(int)
        greater = defaultdict(int)
        result = 0
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1  # no. of elements after i that are greater than i

                else:
                    lesser[i] += 1  # no. of elements after i that are greater than i

        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating)):

                if rating[j] > rating[i]:
                    result = result + greater[j]
                else:
                    result = result + lesser[j]
        return result

obj = Solution()
print(obj.numTeams([2,5,3,4,1]))

