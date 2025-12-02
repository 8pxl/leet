class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

test = Solution()
sol = test.reverseWords("the sky is blue")
print(sol)
