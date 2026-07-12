class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        temp_res = 1
        answer = []
        for j in range(len(nums)):
            for i in range(len(nums)):
                if i == j :
                    continue
                else:
                    temp_res = temp_res * nums[i]
            answer.append(temp_res)
            temp_res = 1
        return answer