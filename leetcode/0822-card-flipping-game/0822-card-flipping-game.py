class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        poss = [True] * 2001
        ans = 2001

        for i in range(n):
            if fronts[i] == backs[i]:
                poss[fronts[i]] = False

        for i in range(n):
            if (poss[fronts[i]]):
                ans = min(ans, fronts[i])
            if (poss[backs[i]]):
                ans = min(ans, backs[i])

        return ans if ans < 2001 else 0


        