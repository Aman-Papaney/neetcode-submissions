class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            temp: dict = {}
            ans = []
            for i in nums:
                if i not in temp:
                    temp[i] = 1
                else:
                    temp[i] += 1
            
            pair = list(temp.items())

            pair.sort(key = lambda x : x[1], reverse = True)

            for i in range(k):
                ans.append(pair[i][0])
            return ans
