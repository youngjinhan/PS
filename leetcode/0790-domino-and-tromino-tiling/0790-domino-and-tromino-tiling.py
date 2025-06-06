class Solution:
    mod = 10**9+7

    def multiply(self, A, B):
        C = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                s = 0
                for k in range(3):
                    s = (s + A[i][k]*B[k][j]) % self.mod
                C[i][j] = s
        return C

    def power(self, base, exp):
        result = [[1,0,0],[0,1,0],[0,0,1]]
        while exp > 0:
            if exp & 1:
                result = self.multiply(result, base)
            base = self.multiply(base, base)
            exp >>= 1
        return result

    def numTilings(self, n):
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        t = [[2,0,1],[1,0,0],[0,1,0]]
        p = self.power(t, n-2)
        return (p[0][0]*2 + p[0][1] + p[0][2]) % self.mod
    # def numTilings(self, n: int) -> int:
        

        
        '''
        n = 1 -> 1
        n = 2 -> 1 + 1
        n = 3 -> 2 + 1 + 2
        n = 4 -> 5 + 2*2 + 1*2
        n = 5 -> 11 + 5*2 + 2*2
        n = 6 -> 25 + 11*2 + 5*2
        '''
        '''
        n=3 -> f(n-1) + f(n-2) + f(n-3) * 2
        '''
        return 25