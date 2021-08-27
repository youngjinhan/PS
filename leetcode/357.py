class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp=[0 for _ in range(10)]
        print(dp)
        dp[0]=1
        dp[1]=dp[0]+9
        dp[2]=dp[1]+9*9
        for i in range(3,10):
            dp[i]+=dp[i-1]
            tmp=9
            cur=1
            fac=9
            while cur<i:
                fac*=tmp
                tmp-=1
                cur+=1
            dp[i]+=fac
        return dp[n]
