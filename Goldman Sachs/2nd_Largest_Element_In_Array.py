class Solution:
    # K= 2
    def second_largest(self, nums):
        first_largest = float("-inf")
        second_largest = float("-inf")

        for i in range(len(nums)):
            if nums[i] > first_largest:
                second_largest = first_largest
                first_largest = nums[i]

            else:
                if nums[i] > second_largest:
                    second_largest = nums[i]
        return second_largest

obj = Solution()
print(obj.second_largest([3,2,1,5,6,4]))