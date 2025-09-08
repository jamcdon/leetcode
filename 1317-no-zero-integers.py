# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

#    a and b are No-Zero integers.
#    a + b = n

#The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1,n):
            j  = n - i
            if '0' not in str(j) and '0' not in str(i):
                return [i,j]

solution = Solution()

ints = [100, 45, 77, 23, 2, 1500, 7777, 25000]

for intt in ints:
    print(solution.getNoZeroIntegers(intt))
