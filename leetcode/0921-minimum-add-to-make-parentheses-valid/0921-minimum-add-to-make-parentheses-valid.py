class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        pos = 0
        nag = 0
        for c in s:
            if c == '(':
                pos += 1
            elif pos > 0:
                pos -= 1
            else:
                nag += 1

        return pos + nag

        