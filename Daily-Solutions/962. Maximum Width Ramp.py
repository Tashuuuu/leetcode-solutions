# Q: A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i. Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

# Solution:
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        new = []
        ans = 0
        for i, num in enumerate(nums):
            if not new:
                new.append(i)
            else:
                if num < nums[new[-1]]:
                    new.append(i)
        for j in range(len(nums)-1,-1,-1):
            while new and nums[new[-1]] <= nums[j]:
                ans = max(ans, j - new.pop())
        return ans
