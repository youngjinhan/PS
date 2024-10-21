class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        tmp = ""
        n = len(target)
        tar = list(target)
        a = 'a'
        for t in tar:
            for i in range(ord(t)-ord(a)+1):
                ans.append(tmp+(chr(ord(a)+i)))
            tmp += t
        return ans



        