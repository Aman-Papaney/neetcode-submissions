class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        temp = set(nums)
    
        for i in temp:
            if (i - 1) not in temp:
                count = 1
                while (i + 1) in temp:
                    i += 1
                    count += 1
                max_seq = max(max_seq, count)
        return max_seq