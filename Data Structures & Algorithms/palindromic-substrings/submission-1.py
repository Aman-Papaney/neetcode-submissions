class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) in (0, 1):
            return len(s)
        max_len = 0
        ans = ''
        count = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                count += 1
                if max_len < (r - l + 1):
                    ans = s[l:r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                count += 1
                if max_len < (r - l + 1):
                    ans = s[l:r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

        return count 