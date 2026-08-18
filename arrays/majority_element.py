# O(n) time; O(n) space — up to n distinct keys this time, no 26-cap: the input is integers, not letters
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            
        for j in count:
            if count[j] > len(nums) // 2:
                return j



if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))     # 3
    print(sol.majorityElement([2,2,1,1,1,2,2]))   # 2
    print(sol.majorityElement([1,1,1,2,2,2,2]))  # 2
  