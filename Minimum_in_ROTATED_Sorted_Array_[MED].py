class Solution:

    def find_minimum(self,nums):
        left = 0
        right = len(nums)-1

        while(left<right):
            # because when left == right, at that position, we have our minimum element, hence come out of while loop
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                # i.e minimum lies on right side of list, search there
                left = mid +1

            else:
                # nums[mid] <=nums[right]
                right = mid
        # exit when left and right overlap i.e left ==right
        return nums[left]    #or nums[right]



obj = Solution()
minimum = obj.find_minimum([3,4,5,1,2])
print(minimum)

