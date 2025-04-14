class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def fast_pow(x, y):
            mul, ret = x, 1
            
            while y > 0:
                if y % 2 == 1:
                    ret = ret * (mul % mod) % mod
                mul = mul * (mul % mod) % mod
                y //= 2
            return ret

        return fast_pow(5, (n+1) // 2) * fast_pow(4, n // 2) % mod
