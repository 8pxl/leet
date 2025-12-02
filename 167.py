class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)-1):
            lo = i+1
            hi = len(numbers)-1
            print("index ", i)
            while (lo <= hi):
                mid = (lo + (hi-lo) // 2)
                sum = (numbers[i] + numbers[mid])
                if sum == target:
                    return([i+1, mid+1])
                if sum < target:
                    lo = mid+1
                else:
                    hi = mid-1

test = Solution()
sol = test.twoSum([3,24,50,79,88,150,345],200)
print(sol)


