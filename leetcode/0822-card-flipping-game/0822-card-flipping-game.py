class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cand = set()
        to_be_removed = set()
        n = len(fronts)

        for i in range(n):
            if fronts[i] == backs[i]:
                to_be_removed.add(fronts[i])
                continue
            cand.add(fronts[i])
            cand.add(backs[i])

        ans = sorted(list(cand - to_be_removed))

        return 0 if len(ans) == 0 else ans[0]