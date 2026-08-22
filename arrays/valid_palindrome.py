# Valid Palindrome — https://leetcode.com/problems/valid-palindrome/
# Two pointers converging; junk skipped in stride, never removed
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