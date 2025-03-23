from collections import defaultdict
from collections import deque

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        connect = defaultdict(list)
        visited = [False] * n
        for i in range(n-1):
            for j in range(i+1, n):
                c = set(properties[i]) & set(properties[j])
                if len(c) >= k:
                    connect[i].append(j)
                    connect[j].append(i)

        # print(connect)
        ans = 0
        for i in range(n):
            if visited[i]:
                continue
            ans += 1
            # print("{}번째".format(i))
        
            q = deque([i])
            visited[i] = True
            while q:
                x = q.popleft()
                # print(x)
                if len(connect[x]) > 0 :
                    for c in connect[x]:
                        if visited[c]:
                            continue
                        visited[c] = True
                        q.append(c)
                        
        return ans