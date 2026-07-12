class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        temp = {}

        for i in strs:
            key = ''.join(sorted(i))
            if key not in temp:
                temp[key] = [i]
            else:
                temp[key].append(i)
        
        return (list(temp.values()))