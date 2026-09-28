


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
       slow = 0
       for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1
       


if __name__ == "__main__":
    sol = Solution()
    a = [0, 1, 0, 3, 12]   # [1, 3, 12, 0, 0]
    sol.moveZeroes(a)       
    print(a)    
    b = [0, 0, 1, 5, 7, 8, 9]
    sol.moveZeroes(b)
    print(b)   # [1, 5, 7, 8, 9, 0, 0]
    c = [0]
    sol.moveZeroes(c)
    print(c)   # [0]                                   
                              



# Time - each element gets touched once, non zeroes get one extra O(1) swap
# Space - nothing grows, in place mutation O(1)