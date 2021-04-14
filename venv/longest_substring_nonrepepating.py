def lengthOfLongestSubstring(s):
    maxlen = 0
    string = ""
    cnt = 0
    i = 0
    j = 0
    if not s:
        return 0

    while (i < len(s)):

        if s[i] not in string:
            string = string + s[i]
            cnt += 1
            # print(cnt, s[i])
            i += 1

        else:
            cnt = 0
            string = ""
            j += 1
            i = j
            # print(i)

        if cnt > maxlen:
            maxlen = cnt

    return maxlen

print(lengthOfLongestSubstring("abcabcbb"))