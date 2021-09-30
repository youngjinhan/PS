class Solution:
    def countSubstrings(self, s: str) -> int:
        # 앞에서부터 하나씩 늘려가며 체크
        '''
        result=len(s)
        
        leng=2
        while leng<=len(s):
            for i in range(len(s)):
                if i+leng>len(s):       
                    continue
                s_test=s[i:i+leng]
                if s_test==s_test[::-1]:
                    result+=1
            leng+=1
        return result
        '''
    
    
        # 가운데 문자부터 앞뒤로 늘려가며 체크
        '''
        count = 0
        for i in range(len(s)):
            # Every char is a palindrome
            count += 1
            # Even length
            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:         # bab i=1 start=1, end=2
                count += 1
                start -= 1
                end += 1
                
            # Odd-length
            start = i - 1
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
        return count
        '''
    
        n = len(s)
        res = 0
        dp = [[0]*(n) for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):                               
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):      
                    dp[i][j] = 1                                
                else:                                          
                    dp[i][j] = 0

                if dp[i][j]:
                    res+=1
        return res 
