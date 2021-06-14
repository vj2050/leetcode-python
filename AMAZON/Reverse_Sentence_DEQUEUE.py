'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single
space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        queue, word = [], []
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                queue.insert(0, ''.join(word))  # .insert(0,value) works like append left
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        queue.insert(0, ''.join(
            word))  # for the last word, there is n ot going to be any leading space, hence wont enter the if loop, hence this additional condition necessary

        return ' '.join(queue)

obj = Solution()
print(obj.reverseWords("the sky is blue"))