class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp_stack = []
        temp = 0
        op_array = ['+','-','*','/']
        
        for i in tokens:
            if i not in op_array:
                temp_stack.append(int(i))
            else:
                if i == '+':
                    temp = temp_stack[-2] + temp_stack[-1]
                elif i == '-':
                    temp = temp_stack[-2] - temp_stack[-1]
                elif i == '*':
                    temp = temp_stack[-2] * temp_stack[-1]
                elif i == '/':
                    temp = int(temp_stack[-2] / temp_stack[-1])
                
                _ = temp_stack.pop()
                _ = temp_stack.pop()
                temp_stack.append(temp)
                    
        return temp_stack[-1]