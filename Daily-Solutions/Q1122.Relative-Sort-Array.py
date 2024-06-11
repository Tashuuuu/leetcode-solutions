# https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans1 = []
        nums = []
        i = 0
        while i < len(arr2):
            if arr2[i] in arr1:
                count = arr1.count(arr2[i])
                while count != 0:
                    ans1.append(arr2[i])
                    count -= 1
            i += 1
        j = 0
        while j < len(arr1):
            if arr1[j] not in arr2:
                nums.append(arr1[j])
            j += 1
        print("ans1 =", ans1)
        print("nums = ", nums)
        def insertion_sort(array):
            def swap(first, second):
                temp = array[first]
                array[first] = array[second]
                array[second] = temp
            i = 0
            while i <= (len(array) - 2): # OR i < len(array) - 1
                j = i + 1
                while j > 0:
                    if array[j] < array[j-1]:
                        swap(j, j-1)
                    else:
                        break
                    j = j - 1
                i = i + 1
            return array
        ans2 = insertion_sort(nums)
        print("ans2 =", ans2)
        ans1.extend(ans2)
        print("total =", ans1)
        return ans1
