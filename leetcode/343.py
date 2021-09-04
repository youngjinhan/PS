class Solution:
    def integerBreak(self, n: int) -> int:

#         if n<4:
#             return n-1
#         elif n==4:
#             return n
        
#         result=1
#         while n-3>1:  n => 3
#             n-=3
#             result*=3
#         return result*n

    '''
    dp[1]=0
    dp[2]=1
    dp[3]=2     1+2 => 2*1=2
    dp[4]=4     1+3, 2+2 => 2*2=4
    dp[5]=6     1+4, 2+3 => 2*3=6
    dp[6]=9     1+5, 2+4, 3+3, 1+3+2 =>  3*3=9
    dp[7]=12    2+2+3, 3+4
    dp[8]=18    2+2+2+2, 3+3+2, 
    dp[9]=27
    dp[10]=36
    dp[11]=54
    '''
    
    '''
    dp=[0 for _ in range(59)]
        if n<4:
            return n-1
        dp[4]=4
        dp[5]=6
        dp[6]=9
        for i in range(7,59):
            dp[i]=3*dp[i-3]
        
        return dp[n]
    '''
        if n<4:
            return n-1
        if n % 3 == 0:
            return pow(3, n // 3)  
        if n % 3 == 1:
            return pow(3, (n // 3) - 1) * 4     
        return pow(3, n // 3) * 2 # n % 3 == 2
        
    
