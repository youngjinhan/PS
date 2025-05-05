from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for d in dominoes:
            cnt[tuple(sorted(d))] += 1

        return sum([c * (c-1) // 2 for c in cnt.values()])
        
        # n = len(dominoes) - len(d_set) + 1
        # return n * (n-1) // 2
        