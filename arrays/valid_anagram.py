# Valid Anagram — https://leetcode.com/problems/valid-anagram/
# Hashmap counting: tally s, spend on t
# Time: O(n) — and O(n) is the floor: every char must be read at least once
# Space: O(1) — dict caps at 26 lowercase keys regardless of n
# Alt: return sorted(s) == sorted(t) — O(n log n), production-fine, interview opener


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in s_counts:
                s_counts[ch] += 1
            else:
                s_counts[ch] = 1
        for ch in t:
            if ch in s_counts and s_counts[ch] > 0:
                s_counts[ch] -= 1
            else:
                return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("ab", "aa"))            # False — the counts case
    print(sol.isAnagram("a", "ab"))             # False — the gate