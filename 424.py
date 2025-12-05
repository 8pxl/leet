import time


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans, maxf = 0,0,0
        map: dict[str,int] = dict()
        for r in range(len(s)):
            map[s[r]] = 1 + map.get(s[r], 0)
            maxf = max(maxf, map[s[r]])
            while ((r-l+1) - maxf > k):
                map[s[l]] -=1
                l+=1
            ans = max(ans, r-l+1)
        return ans
        # left, right, ans= 0,0,0
        # map: dict[str, int] =  dict()
        # targ = s[0]
        # while left <= right < len(s):
        #     char = s[right]
        #     if (char not in map):
        #         map[char] = 1
        #     else:
        #         map[char] += 1
        #     if map[char] > map[targ]:
        #         targ = char
        #     length = right+1-left
        #     if length - map[targ] > k:
        #         map[s[left]] -= 1
        #         left += 1
        #     else:
        #         ans = max(ans, length)
        #     right += 1
        # return ans


test = Solution()
curr = time.time()
sol = test.characterReplacement("ABAB", 0)
print("finished in ", time.time() - curr)
print(sol)
