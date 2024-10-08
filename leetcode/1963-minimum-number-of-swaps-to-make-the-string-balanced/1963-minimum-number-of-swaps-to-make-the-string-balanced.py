class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        for c in s:
            if c == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)

        return len(stack) // 4 if len(stack) % 4 == 0 else len(stack) // 4 + 1