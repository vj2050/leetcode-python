'''
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''
class Solution:
    def minSubArrayLen(self, target, nums):
        i, j = 0, 0
        summ = 0
        minimal_length = float("inf")

        while (j < len(nums)):
            summ += nums[j]
            while (summ >= target):
                minimal_length = min(minimal_length, j + 1 - i)
                summ -= nums[i]  # moving the window from left to right
                i += 1
            j += 1  # j is position 6 at this point.

        if minimal_length == float("inf"):
            return 0
        return minimal_length

obj = Solution()
print(obj.minSubArrayLen(7,[2,3,1,2,4,3]))