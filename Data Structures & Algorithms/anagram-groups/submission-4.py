class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}

        for word in strs:
            sort_ = ''.join(sorted(word))
            if sort_ not in ans:
                ans[sort_] = [word]
            else:
                ans[sort_].append(word)
        return (list(ans.values()))