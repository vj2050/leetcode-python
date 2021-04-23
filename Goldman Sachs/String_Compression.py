class Solution:
    def compress(self, chars):
        if len(chars) == 1:
            return 1
        i, j = 0, 1
        index = 0
        while j < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            chars[index] = chars[i]
            index += 1
            # if count is 2 digit, then split and display
            if j - i > 1:    # j -1 contains actual occurrences of that char
                val = str(j - i)
                for i in val:
                    chars[index] = i
                    index += 1
            i = j
        print(chars[:index])
        return index          # not returning len of chars, since index stores the actual count/ length of chars modified
obj = Solution()
print(obj.compress(["a","a","b","b","c","c","c"]))
print(obj.compress(["a","a","a","a","a","a","a","a","a","a","b","b","c","c","c"]))