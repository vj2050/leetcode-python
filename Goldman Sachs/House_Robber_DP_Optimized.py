# OPTIMIZED DYNAMIC PROGRAMMING APPROACH : always start from "if you had 0 houses, and build on. Here instead of building DP table, used two variables and chaged them each time to avoid space.
# Time Complexity O(n)
# Reduced Space Complexity to O(1) since not using DP table to store values.

class Solution:
    def rob(self, nums):
        max_amount = 0
        amount = 0

        #  Base Cases :
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            # 1 house
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # # create an empty array "dp" also called as DP Table of fixed length = len(nums)
        # dp = [None for i in range(len(nums))]
        # # each element in dp array = max profit upto the i th house
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            current = max((nums[i] + first), second)
            # dp = [2,7,11,11,12]
            first = second
            second = current
        return second

obj = Solution()
print(obj.rob([2,7,9,3,1]))