'''
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
'''

class Solution:
    def maxSubArrayLen(self, nums, k):
        maxLength = float("-inf")
        accumulatedSum = 0
        mydict = {0: -1}

        for i in range(len(nums)):
            accumulatedSum += nums[i]

            if accumulatedSum not in mydict:
                mydict[accumulatedSum] = i  # accu sum till that index : index
            if accumulatedSum - k in mydict:
                maxLength = max(maxLength, i - mydict[accumulatedSum - k])
        if maxLength == float("-inf"):
            return 0
        return maxLength

obj = Solution()
print(obj.maxSubArrayLen([1,-1,5,-2,3],3))