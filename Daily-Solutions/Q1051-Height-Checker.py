# Question link: https://leetcode.com/problems/height-checker/description/?envType=daily-question&envId=2024-06-10
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = list(map(int, heights)) # Create a new list of integers
        expected.sort() # Sorting it in ascending order
        ans = 0
        i = 0
        while i < len(heights):
            if heights[i] != expected[i]:
                ans += 1
            i += 1
        return ans
