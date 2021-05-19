'''
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
'''

from collections import Counter
class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False

        dictt = Counter(nums)
        for key in sorted(dictt):
            if dictt[key] > 0:  # available

                need = dictt[key]
                for i in range(key, key + k):
                    if dictt[i] >= need:
                        dictt[i] = dictt[i] - need
                    else:
                        return False  # not available to utilize
        return True

obj = Solution()
print(obj.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11],3))
