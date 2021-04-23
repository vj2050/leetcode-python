'''
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
'''
class Solution:
    def trap(self, height):
        leftmax = []
        rightmax = []
        left = 0
        right = 0
        result = 0

        for i in height:
            left = max(left, i)
            leftmax.append(left)

        for i in range(len(height) - 1, -1, -1):
            right = max(right, height[i])
            rightmax.append(right)

        rightmax = rightmax[::-1]
        # reverse again so that original order is maintained
        # print(rightmax)

        for i in range(len(height)):
            # calculating water level at each block (i)
            result = result + (min(leftmax[i], rightmax[i]) - height[i])
        return result


obj = Solution()
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))