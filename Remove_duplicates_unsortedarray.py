class Solution:

    def duplicate_remove(self, nums):
        nums.sort()
        print(nums)
### METHOD 1 :
        # i = 0
        # j = 1
        # index = 1
        # prev = nums[0]
        # length = 1

        # for i in range(1,len(nums)):
        #     if nums[i] != prev:
        #         length +=1
        #         nums[index] = nums[i]
        #         index+=1
        #         prev = nums[i]
        # return length

### METHOD 2 SUBMITTED :  More faster Time complextiy : O(n)O(n). Assume that n is the length of array. Each of i and j traverses at most n steps. Space complexity : O(1).

        # i, j = 0, 1
        # while (j < len(nums)):
        #     if nums[i] != nums[j]:
        #         i += 1
        #         nums[i] = nums[j]
        #
        #     j += 1
        #
        # return i + 1  # since index +1 = length

######## Just in case if we want to return the updated unique array instead of just the length of unique array : start from the end, easier to pop/ del elements in list
                    #  start, end, step size (-1 means reverse) Time Complexity : O(n) i travels at the MOST "n" STEPS
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
                print("everytime", nums)
        return nums


obj = Solution()
length = obj.duplicate_remove([1,2,3,2,1,2])
print(length)



