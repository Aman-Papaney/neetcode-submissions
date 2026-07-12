class Solution:
    
    def isPalindrome(self,s: str) -> bool:
        ans : bool = True
        # temp : str = ''
        temp2 : str = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890'
        
        
        size : int = len(s)
        left : int = 0
        right : int = size - 1 
        while left < right:
            if s[left] not in temp2:
                left += 1
            elif s[right] not in temp2:
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return ans
        
# print(isPalindrome("0P"))