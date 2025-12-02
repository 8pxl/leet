import time


class Solution:
    def maxArea(self,height: list[int]) -> int:
        h = height
        n = len(h)
        left, right, area, minHeight, width = 0, len(h)-1, 0, 0
        while (left < right):
            hl = h[left]
            hr = h[right]
            mlr = 0
            if (hl < hr):
                mlr = hl
            else:
                mlr = hr
            if (mlr > minHeight):
                candArea = (right - left) * mlr
                if candArea > area:
                    area = candArea
                    minHeight = mlr
            if (hl < hr):
                left += 1
            else:
                right -= 1
        return area


test = Solution()
start = time.time()
sol = test.maxArea([1,8,6,2,5,4,8,3,7])
print(time.time() - start)
print(sol)

# the kind of "intution" is that what you previously checked doesn't really matter, since you already start with the "theoretical max" and each continuous step basically will have been the best option you couldve taken so you don't really need to return to what you have and recheckg
# removing the smaller of the 2 is important, because if you remove the bigger one then theoretically the smaller side couldve encounted something bigger etc
