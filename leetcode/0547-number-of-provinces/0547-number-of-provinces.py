from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        isVisited = [False] * n
        ans = 0

        queue = deque()

        for i in range(n):
            if isVisited[i]:
                continue
            ans += 1
            queue.append(i)
            isVisited[i] = True
            while queue:
                v = queue.popleft()
                for j in range(n):
                    if i != j and isConnected[v][j] and isVisited[j] == False:
                        queue.append(j)
                        isVisited[j] = True
        
        return ans
