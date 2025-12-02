class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        curr = 0
        if not s:
            return True
        while (left <= right < len(t)):
            if not (t[left] == s[0]):
                left += 1
                right = left
                continue
            if t[right] == s[curr]:
                if curr == (len(s) - 1):
                    return True
                curr += 1
                right += 1
            else:
                if right == (len(t) - 1):
                    left += 1
                    right = left
                    curr = 0
                else:
                    right += 1
        return False


test = Solution()
sol = test.isSubsequence("b", "abc")
print(sol)


