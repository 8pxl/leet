class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ln = len(nums)
        #set is valid bc:equalf
        sols: set[tuple[int,int,int]] = set()
        print(nums)
        for i in range(ln-1):
            left = i+1
            right = ln-1
            print("checking: ", i)
            curr = nums[i]
            while (left < right):
                print(nums[left], nums[right])
                sum = nums[left] + nums[right]
                if not (curr + sum):
                    sols.add((curr, nums[left], nums[right]))
                    left += 1
                elif (sum > (-1*curr)):
                    right -= 1
                else:
                    left += 1
        return(list(map(list,tuple(sols))))


test = Solution()
sol = test.threeSum([-100,-70,-60,110,120,130,160])
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
# lets say we've arrived at a solution, how do we know weather we should start or if there will be a solution in thefuture as well?
# ok well there 2 cases, either we find more numbers that sum up to our base number, in which ase the numbers cant be repeated? is that true 



