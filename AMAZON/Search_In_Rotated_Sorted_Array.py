'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at
pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''

class Solution:
    # Compare MID with START and then compare with target to set search scope
    def search(self, nums, target):
        mid = 0
        left, right = 0, len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            # cond 1 check if mid elem is > leftmost : hence l.h.s sub part is non rotated
            if nums[mid] >= nums[left]:
                # search if target located in this range else, r.h.s
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    # r.h.s search
                    left = mid + 1
            else:
                # nums[mid] < nums[start]: r.h.s will have non-rotated subarray, easier to check ahead if target lies in this non rotated range
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
