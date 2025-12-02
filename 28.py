class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        right = 0
        left = 0
        while left <= right < len(haystack):
            if haystack[right] == needle[right-left]:
                if (right-left == len(needle)-1):
                    return left
                right += 1
            else:
                left +=1
                right = left
        return -1


test = Solution()
sol = test.strStr("ppi", "pi")
print(sol)
