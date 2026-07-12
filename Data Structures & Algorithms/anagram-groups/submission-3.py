class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def convert_to_freqarr(word):
            temp = [0 for i in range(26)]
            for i in word:
                temp[ord(i) - ord('a')] += 1
            return temp

        res = {}

        for word in strs:
            freq = tuple(convert_to_freqarr(word))
            if (freq) not in res:
                res[freq] = [word]
            else:
                res[freq].append(word)
        return list(res.values())




    