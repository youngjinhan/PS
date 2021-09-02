class Solution:
    def integerBreak(self, n: int) -> int:

        if n<4:
            return n-1
        elif n==4:
            return n
        
        result=1
        while n-3>1:  n => 3
            n-=3
            result*=3
        return result*n
