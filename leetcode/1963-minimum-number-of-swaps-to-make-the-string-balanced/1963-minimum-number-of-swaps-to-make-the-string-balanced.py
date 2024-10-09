class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
        return (ans + 1) // 2


        ''' my solution
        
        stack = []

        for c in s:
            if c == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)

        return (len(stack) // 2 + 1) // 2
        '''