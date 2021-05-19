'''
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Try thinking of it as being in one of two states: have yet to delete an element, and already deleted one element.
currentMax is the state where we have yet to delete any elements. For currentMax, we either add the current value to the previous currentMax, OR we start our subarray over and just use arr[i].
In the above solution, delete is the "already deleted one element" state.
There's two ways we can get to that delete state: using the value of our previous currentMax state and deleting the current element (which is the same thing as not including the element in the sum)
and we can do this because in the currentMax state we are allowed to delete something, OR we can add the current element to the previous delete state.
This is why we can never "delete more than one element in the array", because the previous delete is not included as an option for the Math.max, only delete + arr[i] and currentMax are.

'''

class Solution:
    def maximumSum(self, arr):
        currentMax = arr[0]
        delete = arr[0]
        result = arr[0]

        for i in range(1, len(arr)):
            delete = max(currentMax, delete + arr[i])
            currentMax = max(arr[i], arr[i] + currentMax)

            result = max(result, delete, currentMax)
        return result
obj = Solution()
print(obj.maximumSum())