import time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        chars: dict[int, int] = dict() 
        while (left <=right < len(s)):
            print(s[left:right+1])
            char = ord(s[right])
            if char not in chars.keys():
                chars[char] = right
                right += 1
            else:
                left = chars[char]+1
                chars = dict()
                right = left
            ans = max(ans, len(chars.keys()))
        return ans


test = Solution()
curr = time.time()
sol = test. lengthOfLongestSubstring("abcabcbb")
print("finished in ", time.time() - curr)
print(sol)
