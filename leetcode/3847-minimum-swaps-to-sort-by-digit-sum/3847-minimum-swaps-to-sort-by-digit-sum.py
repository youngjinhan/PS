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


        '''
        digit_sums = [None] * n
        visited = [False] * n

        for i in range(n):
            digit_sums[i] = [i, nums[i], digit_sum(nums[i])]

        sorted_digit = sorted(digit_sums, key = lambda x: (x[2], x[1]))
        # print(sorted_digit)
        
        
        for i in range(n):
            cur = i
            if visited[cur]:
                continue
            visited[cur] = True
            while cur != sorted_digit[cur][0] and not visited[sorted_digit[cur][0]]:
                cur = sorted_digit[cur][0]
                visited[cur] = True
                ans += 1
                
        return ans
        '''