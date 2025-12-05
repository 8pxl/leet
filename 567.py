import time


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perms: dict[str, int] = dict()
        for char in s1:
            perms[char] = 1 + perms.get(char, 0)
        left = 0
        print(perms)
        count = 0
        check: dict[str,int] = dict()
        for right in range(0, len(s2)):
            print(s2[left:right+1])
            char = s2[right]
            check[char] = 1 + check.get(char, 0)
            if (check[char] - perms.get(char, check[char] + 1) == 0):
                count += perms[char]
            print(check, count)
            if count == len(s1):
                return True

            if (right < len(s1)-1):
                continue
            leftChar = s2[left]
            if leftChar in perms:
                if (check[leftChar] - perms[leftChar] == 0):
                    count -= perms[leftChar]
            check[leftChar] -= 1
            left += 1
        return False


test = Solution()
curr = time.time()
sol = test.checkInclusion("ab", "eidboaoo")
print("finished in ", time.time() - curr)
print(sol)
