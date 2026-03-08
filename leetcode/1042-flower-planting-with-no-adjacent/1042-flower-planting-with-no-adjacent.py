from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        bi = defaultdict(list)
        for x, y in paths:
            bi[x].append(y)
            bi[y].append(x)

        ans = [None] * (n+1)

        for i in range(1, n+1):
            to_be_removed = [ans[j] for j in bi[i] if ans[j] != None]
            cand = [x for x in [1,2,3,4] if x not in to_be_removed]
            ans[i] = cand[0]

        return ans[1:]

            
        