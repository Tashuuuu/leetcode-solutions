# https://leetcode.com/problems/patching-array/?envType=daily-question&envId=2024-06-16

def minPatches(self, nums: List[int], n: int) -> int:
  miss = 1
  result = 0
  i = 0
  while miss <= n:
    if i < len(nums) and nums[i] <= miss:
      miss += nums[i]
      i += 1
    else:
      miss += miss
      result += 1
  return result
