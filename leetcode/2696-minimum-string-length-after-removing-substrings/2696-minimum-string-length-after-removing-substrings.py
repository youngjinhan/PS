class Solution:
    def minLength(self, s: str) -> int:
        cand = ["AB", "CD"]
        while cand[0] in s or cand[1] in s:
            if cand[0] in s:
                s = s.replace(cand[0], "")
            else:
                s = s.replace(cand[1], "")
        return len(s)
        