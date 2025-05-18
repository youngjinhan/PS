class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = 0
        def digit_sum(n):
            return sum(map(int, str(n)))
        
    
        n = len(nums)
        visited = [False] * n
        sums = [[digit_sum(val), val, i] for i, val in enumerate(nums)]
        sums.sort()

        for i in range(n):
            if i == sums[i][2] or visited[i]:
                continue
            
            cycle_size = 0
            
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = sums[cur][2]
                cycle_size += 1

            if cycle_size > 1:
                ans += (cycle_size -1)
        return ans