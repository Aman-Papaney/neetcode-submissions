class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            temp: dict = {}
            ans = []
            length: int = len(nums)
            cou: int = 0
            for i in nums:
                if i not in temp:
                    temp[i] = 1
                else:
                    temp[i] += 1
            
            pair = list(temp.items())
            buckets = [[] for j in range(length + 1)]

            for key, values in temp.items():
                buckets[values].append(key)

            for i in range(len(buckets) - 1, 0, -1):
                for n in buckets[i]: 
                    ans.append(n)
                    if len(ans) == k:
                        return ans

