'''   BRUTE FORCE
def checkPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1
    while (i < j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def countSubstrings(self, s: str) -> int:
    output = len(s)

    for i in range(len(s)):
        for j in range(i + 1, len(s)):

            substring = s[i:j + 1]
            print("substring ", substring)
            # check palindrome
            if self.checkPalindrome(substring):
                output += 1

    return output
'''



