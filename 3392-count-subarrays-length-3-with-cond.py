# 3392. Count Subarrays of Length Three With a Condition

# Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        count = 0
        for i in range(1, len(nums) - 1):
            if 2 * (nums[i-1] + nums[i+1]) == nums[i]:
                count += 1
        return count

solution = Solution()

arrays = [[1,2,1,4,1], [1,1,1]]

for array in arrays:
    print(solution.countSubarrays(array))
