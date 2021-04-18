# DP Approach, similar to House Robber problem
# Input [2,2,3,3,3,4] Output : 9

class Solution:
    def deleteAndEarn(self, nums):
        maxx = max(nums)
        dic = [0] * (maxx + 1)
        dp = [0] * (maxx + 1)  # DP table:
        # storing total score of each value, here i reflects the element from nums[] and dic[i] = total score
        for i in nums:
            dic[i] = dic[i] + i
        print(dic)
        dp[0] = 0
        dp[1] = dic[1]  # will start from 1 since key !=0, since points cannot be 0
        for i in range(2, maxx + 1):
            dp[i] = max(dic[i] + dp[i - 2], dp[
                i - 1])  # max between if chosen (current total score+max_score upto i-2th location) OR (take max_score upto i-1 th location)
        print(dp)
        return dp[maxx]

obj = Solution()
print(obj.deleteAndEarn([2,2,3,3,3,4]))