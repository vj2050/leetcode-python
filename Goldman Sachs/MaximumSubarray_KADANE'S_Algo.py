'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

KADANE'S ALGORITHM : https://www.youtube.com/watch?v=86CQq3pKSUw
at each position starting from 1 to n-1, you find the max between current element and current element + previous max subarray sum
'''

class Solution:
    def maxSubArray(self, nums):
        # METHOD 2 KADANE'S Algorithm    O(N)
        currentMax = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            currentMax = max(nums[i], nums[i] + currentMax)

            if currentMax > globalMax:
                globalMax = currentMax
        return globalMax

# #METHOD 1 : O(N)
#         maxSum = float("-inf")
#         summ=0
#         for i in range (len(nums)):
#             summ=summ+nums[i]

#             if summ > maxSum:
#                 maxSum = summ
#             if summ<0:
#                 print("negative sum is ", summ)
#                 summ=0
#             print("summ and maxsum ", summ,maxSum)


#         return maxSum

obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
