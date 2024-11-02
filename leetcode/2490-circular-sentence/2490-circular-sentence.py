class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        cur = 0
        while cur < n:
            if words[cur][-1] != words[(cur+1)%n][0]:
                return False
            cur += 1

        return True
        
