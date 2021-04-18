# SIMPLE DYNAMIC PROGRAMMING APPROACH : always start from "if you had 0 houses, and build on. Here use dp array i.e DP table to store max profit upto ith house each time.
# Time Complexity O(n)
# Space Complexity to O(n) since using DP table to store values.

class Solution:
    def rob(self, nums):
        #  Base Cases :
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            # 1 house
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # create an empty array of fixed length = len(nums)
        dp = [None for i in range(len(nums))]
        # each element in dp array = max profit upto the i th house
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(dp)):
            dp[i] = max((nums[i] + dp[i - 2]), dp[i - 1])
            # dp = [2,7,11,11,12]
        return dp[-1]

obj = Solution()
print(obj.rob([2,7,9,3,1]))




