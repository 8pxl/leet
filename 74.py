import time
from lib import *

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        lo, mid = 0, 0
        hi = len(matrix)-1
        row = -1
        while lo <= hi:
            mid = (lo+hi) >> 1
            r= matrix[mid]
            rmin =r[0]
            rmax =r[-1]
            if rmin > target:
                hi = mid - 1
            elif rmax < target:
                lo = mid + 1
            else:
                row = mid
                break
        if row == -1:
            return False
        lo, mid = 0, 0
        hi = len(matrix[row])-1
        col = -1
        while lo <= hi:
            mid = (lo+hi) >> 1
            val = matrix[row][mid]
            if val > target:
                hi = mid - 1
            elif val < target:
                lo = mid + 1
            else:
                col = mid
                break
        return col != -1


test = Solution()
curr = time.time()
sol = test.searchMatrix([[1,3,5,7]], 1)
print("finished in ", time.time() - curr)
print(sol)
