from collections import defaultdict

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = defaultdict(int)

        n = len(s)

        if n < k: return False
        if n == k: return True

        for c in s:
            count[c] = (count[c] + 1) % 2

        return k >= sum(count.values())

        