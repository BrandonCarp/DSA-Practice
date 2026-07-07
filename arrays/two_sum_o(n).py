class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, i in enumerate(nums):
            j = target - i
            if j in seen:
                return [index, seen[j]]
            seen[i] = index
           
