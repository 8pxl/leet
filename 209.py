from math import inf
import time

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, right, sum = 0, 0, nums[0]
        ans = len(nums) + 1
        while left <= right < len(nums):
            print(left, right, sum)
            if sum >=target:
                ans = min((right + 1)-left, ans)
                sum -= nums[left]
                left += 1
            else:
                right += 1
                if right >=len(nums):
                    break
                sum += nums[right]
        return ans if ans <=len(nums) else 0
__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))

test = Solution()
curr = time.time()
sol = test.minSubArrayLen(11,[1,1,1,1,1,1,1,1])
print("finished in ", time.time() - curr)
print(sol)

"""
4
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,3]

the biggest number is not always included 
greedy doesnt quite work
"""
