from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in numDict:
                return numDict[complement], index
            else:
                numDict[num] = index