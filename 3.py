import time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        chars: dict[str, int] = dict() 
        while (left <=right < len(s)):
            char = s[right]
            if char in chars and (chars[char] >=left):
                left = chars[char]+1
            chars[char] = right
            right+=1
            ans = max(ans, (right+1-left))
        return ans


test = Solution()
curr = time.time()
sol = test. lengthOfLongestSubstring("abcabcbb")
print("finished in ", time.time() - curr)
print(sol)
