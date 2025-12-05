import time


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        map: dict[str, int] = dict()
        for char in t:
            map[char] = 1 + map.get(char, 0)
        check: dict[str, int] = dict()
        targ = len(map)
        l,r,matches, prevr = 0,0,0,-1
        while l <=r < len(s):
            if r != prevr:
                char = s[r]
                if char in map:
                    check[char] = 1 + check.get(char, 0)
                    if check[char] - map[char] == 0:
                        matches += 1
            prevr = r
            if matches == targ:
                lchar = s[l]
                substr = s[l:r+1]
                if (not ans) or (len(substr) < len(ans)):
                    ans = substr
                if lchar in map:
                    if check[lchar] - map[lchar] == 0:
                        matches -= 1
                    check[lchar] -= 1
                l += 1
            else:
                r += 1
        return ans

test = Solution()
curr = time.time()
sol = test.minWindow("aa", "aa")
print("finished in ", time.time() - curr)
print(sol)
