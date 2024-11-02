class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        n = len(s)
        cur = 0
        while cur < n:
            leng = 0
            ch = s[cur]
            while cur < n and s[cur] == ch:
                leng += 1
                cur +=1
            leng = 2 if leng > 2 else leng
            ans += ch * leng
        return ans