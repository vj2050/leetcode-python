# Problem number 22 Medium
# Video reference :  https://www.youtube.com/watch?v=tyVBx-OtDug&ab_channel=KeepOnCoding

class Solution:
    def generateParenthesis(self, n: int):
        # stack = []
        result = []

        def backtrack_recursive(result, str_formed, open_remaining, close_remaining):

            if open_remaining == 0 and close_remaining == 0:  # all brackets used
                result.append(str_formed)
                return  # that is topmost element of stack is popped

            if open_remaining < 0 or open_remaining > close_remaining:
                return  # that is topmost element of stack is popped

            backtrack_recursive(result, str_formed + "(", open_remaining - 1, close_remaining)

            backtrack_recursive(result, str_formed + ")", open_remaining,
                                close_remaining - 1)  # after this we reach the end of function , hence here also the call is resolved, and topmost element of stack is popped

        backtrack_recursive(result, "", n, n)
        return result

obj = Solution()
result = obj.generateParenthesis(3)
print(result)


###### Using Stack Method 2 :
'''
    if opencount == closecount == n:
                res.append("".join(stack))
                return     # return from backtracking function

            if opencount < n:
                # use the open brackets choice till count == n
                stack.append("(")
                backtrack_recursive(opencount+1, closecount)
                stack.pop()

            if closecount < opencount:
                # can use the close brackets now since open ones are exhausted
                stack.append(")")
                backtrack_recursive(opencount, closecount+1)
                stack.pop()
'''