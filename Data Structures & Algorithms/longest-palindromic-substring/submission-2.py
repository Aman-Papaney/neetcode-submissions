class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) in (0, 1):
            return s
        max_len = 0
        ans = ''

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if max_len < (r - l + 1):
                    ans = s[l:r + 1]
                    max_len = max(max_len, r - l + 1)
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if max_len < (r - l + 1):
                    ans = s[l:r + 1]
                    max_len = max(max_len, r - l + 1)
                l -= 1
                r += 1

            
            
        return ans 