class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        #start, end = 0, len(s) - 1

        for i in range(len(s)//2):
            s[len(s)-1-i], s[i] = s[i], s[len(s)-1-i]

        # while (start < end):
        #     temp = s[start]
        #     s[start] = s[end]
        #     s[end] = temp
        #     # direct swapping
        #     start += 1
        #     end -= 1

        return s

obj = Solution()
s = obj.reverseString(["h","e","l","l","o"])
print(s)


