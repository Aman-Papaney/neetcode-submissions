class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp2 = sorted(s1)
        right = len(s1)

        for left in range(len(s2) - len(s1) + 1):
            temp = sorted(s2[left:right])
            if (temp == temp2):
                return True
            right += 1
        return False
