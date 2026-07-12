class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res: list[int] = [0] * len(temperatures)
        temp_stack: list[list[int]] = []

        for i in range(len(temperatures)):
            while temp_stack and temp_stack[-1][1] < temperatures[i]:
                res[temp_stack[-1][0]] = i - temp_stack[-1][0]
                _ = temp_stack.pop() 
            temp_stack.append([i, temperatures[i]])
                
        return res