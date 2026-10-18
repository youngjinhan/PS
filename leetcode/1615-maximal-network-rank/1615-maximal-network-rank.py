from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        connected = defaultdict(list)
        ans = 0

        for a, b in roads:
            connected[a].append(b)
            connected[b].append(a)
        
        for a in connected:
            for b in connected:
                if a == b:
                    continue
                
                tmp = len(connected[a]) + len(connected[b])
                if b in connected[a]:
                    tmp -= 1
                ans = max(ans, tmp)

        return ans