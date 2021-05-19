'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28
Example 3:
'''
class Solution:
    def titleToNumber(self, columnTitle):

        if not columnTitle: return 0
        if len(columnTitle) == 1:
            return ord(columnTitle) - ord('A') + 1
        else:
            ans = 0
            for char in columnTitle:
                ans = (ans * 26) + ord(char) - ord('A') + 1
        return ans

obj = Solution()
print(obj.titleToNumber("AB"))