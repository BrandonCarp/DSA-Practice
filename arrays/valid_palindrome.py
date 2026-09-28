# Valid Palindrome — https://leetcode.com/problems/valid-palindrome/
# Time: O(n) — each pointer crosses the string once between them
# Space: O(n) for the lowered copy — O(1) achievable by lowering at the
#   comparison instead; kept the copy for readability. (The trade, told.)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        s = s.lower()
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else: return False
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
        return True



if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False
    print(sol.isPalindrome(".,"))                              # True 
    print(sol.isPalindrome("0P"))                              # False 

    # Time - left / right start at n-1 apart. every lap the pointers (left/right) move inward
    # Time - even the non .isalnum() push the pointers forward.
    # unless during the "budget" the str returns false
    # Space - s.lower returns back a new 10,000 character string, so there is growth