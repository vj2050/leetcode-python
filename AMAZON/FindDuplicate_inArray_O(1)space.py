'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

'''

class Solution:
    ####### FLOYD'S Tortoise- Hare algorithm ###################
    def findDuplicate(self, nums):
        # use this information : containing n + 1 integers where each integer is in the range [1, n] inclusive
        # this means that the elements value are going to be in range of the indices of array i.e (0, n]
        # start from first index
        tortoise = hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                # intersection point found (not cycle entrance)
                break

        tortoise = nums[0]  # reset to first place, and slow down the hare
        # hare is still at intersection point
        while (tortoise != hare):
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

obj = Solution()
print(obj.findDuplicate([3,1,3,4,2]))

