class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res: list[int] = [0] * len(temperatures)
        temp_stack: list[list[int]] = []

        for i in range(len(temperatures)):
            if len(temp_stack) == 0:
                temp_stack.append([i, temperatures[0]])
                continue
            if temperatures[i] <= temp_stack[-1][1]:
                temp_stack.append([i, temperatures[i]])
                continue
            else:
                while len(temp_stack) > 0 and temp_stack[-1][1] < temperatures[i]:
                    res[temp_stack[-1][0]] = i - temp_stack[-1][0]
                    _ = temp_stack.pop() 
                temp_stack.append([i, temperatures[i]])
                    
        return res