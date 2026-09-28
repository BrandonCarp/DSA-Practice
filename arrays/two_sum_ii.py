from typing import List


# Two pointers on sorted input 
#   sum's verdict eliminates a whole row of pairs. O(n) time, O(1) space — the dict replaced by sortedness
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return left + 1, right + 1
            elif total > target:
                right -= 1
            else:
                left +=1 


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))     #(1,2)
    print(sol.twoSum([3,5,6], 9))   #(1,3)

    # Time  every lap right/left move one pointer inwards, left/right start n-1 apart, 
    # except at the match. at most n-1 laps => O(n). Left/right have a budget which 
    # are the moves allowed before the while becomes false

    # Space nothing grows in two sum ii either, we are just checking the list

  