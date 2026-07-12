class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = (nums)
        temp.sort()
        ans = []
        
        for k in range(0, len(temp) - 2):
            if k > 0 and temp[k] == temp[k - 1]:
                continue
            small: int = k + 1
            large: int = len(temp) - 1
            target = -nums[k]

            while (small < large):
                temp_sum = temp[small] + temp[large]
                if temp_sum > target:
                    large -= 1
                elif temp_sum < target:
                    small += 1
                    
                else:
                    temp2 = [temp[small], temp[large], temp[k]]
                    ans.append(temp2)
                    small += 1
                    large -= 1
                    while small < large and temp[small] == temp[small - 1]:
                        small += 1
            
        return ans