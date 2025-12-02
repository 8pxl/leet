class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ln = len(nums)
        sols = set()
        for i in range(ln):
            left = i
            right = ln-1
        return([[1]])


test = Solution()
sol = test.threeSum([-1,0,1,2,-1,-4])
print(sol)


# want to find unique numbers that sum to 0
# in other words, the indicies sum to equal the negative of the third
#
# [-1,0,1,2,-1,-4]
# -1, 0, 1
# 2, -1, -1
# other than the identity triplet, (0,0,0), each triplet must contain at least one postiitve and one negative value ?
# if we were to sort, [-4,-1,-1,0,1,2]
# we see that there are only like not that many valid triplet set 
# whawt if wejstart from a number, and then see if we can add to it to get 0?
# start with ts left, ()
# if we sort it, can we say that i<j<k ?
# i mean, we can arbitrarily define any triplet such that i < j < k
# meaning we can start wiht an i, look forward for a j and then look forward for a k ?? 
# ok so sort and DONt remove dupes otherwise the identity triplet doesnt work
# or remove dupes that are not 0 ? but then thats not elegatn
# [-4,-1,0,1,1, 2]
# -4 -1 ()
# what else can we say about the solution ?
# one digit must be the biggest 
# if 1 ptr is on -4, and the right ptr is on #2, if its too big then that means that its impossible no ?
# Yes. it does 
# -1, 2 (1, greater than 0, so )
#
# fundementally, i dont get how 
