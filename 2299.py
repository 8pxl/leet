import time
from lib import *

class Solution:
    def strongPasswordCheckerII(self, password:str) -> bool:
        bitmask = int(len(password) >= 8) << 0
        prev = "meow"
        for char in password:
            oc = ord(char)
            bitmask |= int(ord('a') <= oc <= ord('z')) << 1
            bitmask |= int(ord('A') <= oc <= ord('Z')) << 2
            bitmask |= int(ord('0') <= oc <= ord('9')) << 3
            bitmask |= int(char in "!@#$%^&*()-+") << 4
            bitmask |= int(char == prev) << 5
            prev = char
        bitmask ^= (1 << 5)
        return ((bitmask & 0b111111) == 0b111111)


test = Solution()
curr = time.time()
sol = test.strongPasswordCheckerII("0Aa!a!a!")
print("finished in ", time.time() - curr)
print(sol)
