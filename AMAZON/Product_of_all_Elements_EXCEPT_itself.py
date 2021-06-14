class Solution:
    def productExceptSelf(self, nums):

        ### MODIFIED O(1) EXTRA SPACE COMPLEXITY
        length = len(nums)
        answer = [0]* length
        answer[0] = 1     # since no product to the left of index 0
        R =1
        # start saving left products in answer array itself
        for i in range(1,length):
            answer[i] = answer[i-1] * nums[i-1]
        print(answer)
        for j in reversed(range(length)):
            answer[j] = answer[j] * R
            print("answer now", answer[j])
            R = R * nums[j]
            print("R ", R)
        print(answer)










    ##### O(N) Time and Space Complexity
    '''
        length = len(nums)
        leftProd, rightProd = [0] * length, [0] * length
        answer = [0] * length

        leftProd[0] = 1
        rightProd[length - 1] = 1

        for i in range(1, length):
            leftProd[i] = nums[i - 1] * leftProd[i - 1]

        for j in reversed(range(length - 1)):
            rightProd[j] = nums[j + 1] * rightProd[j + 1]
        print("left product ", leftProd)
        print("right product ", rightProd)

        for i in range(length):
            answer[i] = leftProd[i] * rightProd[i]
        return answer
    '''
obj = Solution()
print(obj.productExceptSelf([1,2,3,4]))