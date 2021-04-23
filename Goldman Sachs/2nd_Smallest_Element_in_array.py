class Solution:
    # K= 2
    def second_largest(self, nums):
        first_smallest = float("inf")
        second_smallest = float("inf")

        for i in range(len(nums)):
            if nums[i] < first_smallest:
                second_smallest = first_smallest
                first_smallest = nums[i]

            else:  # if not lesser than first smalles, is it atleast lesser than second smallest?
                if nums[i] < second_smallest:
                    second_smallest = nums[i]
        return second_smallest

obj = Solution()
print(obj.second_largest([3,2,1,5,6,4]))