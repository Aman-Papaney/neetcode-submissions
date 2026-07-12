class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for i in (strs):
            temp = temp + str(len(i)) + '!' + i

        return temp


    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0

        while i < len(s):
        
            length = ''
            while s[i] != '!':
                length += s[i]
                i += 1

            i += 1 

            length = int(length)
            word = s[i:i+length]
            answer.append(word)

            i += length  
        return answer