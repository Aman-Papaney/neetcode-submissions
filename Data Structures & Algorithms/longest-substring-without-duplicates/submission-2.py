class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique: set(str) = set()
        left : int = 0
        result : int = 0

        for right in range(len(s)):
            while (s[right] in unique):
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            result = max(result, right - left + 1)


        return result