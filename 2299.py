import time
from lib import *

class Solution:
    def strongPasswordCheckerII(self, password:str) -> bool:
        bitmask = 0
        bitmask |= (1 if len(password) >= 8 else 0) << 0
        prev = "00"
        for char in password:
            oc = ord(char)
            bitmask |= (1 if ord('a') <= oc <= ord('z') else 0) << 1
            bitmask |= (1 if ord('A') <= oc <= ord('Z') else 0) << 2
            bitmask |= (1 if ord('0') <= oc <= ord('9') else 0) << 3
            bitmask |= (1 if char in "!@#$%^&*()-+" else 0) << 4
            bitmask |= (1 if char == prev else 0) << 5
            prev = char
        bitmask ^= (1 << 5)
        print(bin(bitmask))
        return ((bitmask & 0b111111) == 0b111111)


test = Solution()
curr = time.time()
sol = test.strongPasswordCheckerII("0Aa!a!a!")
print("finished in ", time.time() - curr)
print(sol)
