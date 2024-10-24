class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(array, first, second):
            temp = array[first]
            array[first] = array[second]
            array[second] = temp 
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct]:
                swap(nums, i, correct)
            else:
                i += 1
        j = 0
        while j < len(nums):
            if nums[j] != j+1:
                return j + 1
            j += 1
        return len(nums) + 1
