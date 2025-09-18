#You are given a positive integer num consisting only of digits 6 and 9.
#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

#Example 1:

#Input: num = 9669
#Output: 9969
#Explanation: 
#Changing the first digit results in 6669.
#Changing the second digit results in 9969.
#Changing the third digit results in 9699.
#Changing the fourth digit results in 9666.
#The maximum number is 9969.

class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        for i in range(len(str_num)):
            if str_num[i] == "6":
                str_num = str_num[:i] + "9" + str_num[i+1:]
                break
        return int(str_num)

solution = Solution()

test_cases = [9669, 9996, 9999, 9696969696969696969696]

for test_case in test_cases:
    print(solution.maximum69Number(test_case))
