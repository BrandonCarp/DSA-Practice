# Ransom Note — https://leetcode.com/problems/ransom-note/
# Hashmap counting: tally the note (demand), cancel with magazine (supply), sweep for unmet demand
# — inverse direction of valid_anagram (which tallies supply and spends demand against it)
# Time: O(n + m) — n = note, m = magazine; each string read once
# Space: O(1) — dict caps at 26 lowercase keys regardless of input size


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        if len(ransomNote) > len(magazine):
            return False
        for ch in ransomNote:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        for ch in magazine:
            if ch in count:
                count[ch] -= 1
            
        for i in count:
            if count[i] > 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b"))     # False
    print(sol.canConstruct("aa", "ab"))   # False
    print(sol.canConstruct("aa", "aab"))  # True
    print(sol.canConstruct("ab", "ac"))   # False 