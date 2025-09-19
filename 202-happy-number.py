#Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:

#    Starting with any positive integer, replace the number by the sum of the squares of its digits.
#    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#    Those numbers for which this process ends in 1 are happy.

#Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            str_n = str(n)
            if n == 1:
                return True
            if n == 2 or n == 3 or n == 4:
                return False
            new_n = 0
            for char in str_n:
                new_n += int(char) * int(char)
            n = new_n

solution = Solution()

test_cases = [19, 2, 7, 3, 4, 11, 2940, 123, 686904, 588]
expecteds = [True, False, True, False, False, False, False, False, False, False]

failure = False
for i in range(len(test_cases)):
    if solution.isHappy(test_cases[i]) != expecteds[i]:
        failure == True
        print(f"Error with test case [{i}]. {test_cases[i]} != {expecteds[i]}")
if failure == False:
    print("All test cases passed.")
else:
    print("Errors occured. See above.")
