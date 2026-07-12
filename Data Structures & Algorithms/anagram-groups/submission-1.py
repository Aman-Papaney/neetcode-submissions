class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       

        temp = {}

        for i in strs:
            count = [0] * 26
            for j in i:
                index = ord(j) - ord('a')
                count[index] += 1
            key = tuple(count)

            if key not in temp:
                temp[key] = [i]
            else:
                temp[key].append(i)
        return (list(temp.values()))