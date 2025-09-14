class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sub = set()
        ans = 0
        n = len(s)
        def parse(cand, ls, subset): # (substring, left string, substring set)
            nonlocal ans
            if cand == ls:
                if cand not in subset:
                    ans = max(ans, len(sub) + 1)
                return

            if cand in subset:
                return

            nc = len(cand)
            for i in range(1, n - nc + 1):
                subset.add(cand)
                nls = ls[nc:]
                parse(nls[:i], nls, subset)
                subset.remove(cand)


        parse("", s, sub)

        return ans - 1

        



        