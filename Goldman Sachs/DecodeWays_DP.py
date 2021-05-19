class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]

        dp[0] = 1
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(dp)):  # len of dp

            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            # check for 2 digit combo
            # go 2 digits back in s
            two_digit = int(s[i - 2:i])
            print(two_digit)
            if two_digit >= 10 and two_digit <= 26:
                dp[i] = dp[i] + dp[i - 2]

        return dp[len(s)]

obj = Solution()
print(obj.numDecodings("206"))