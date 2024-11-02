class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        '''
        Solution with O(1) Space complexity
        '''
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[len(sentence) - 1]

        '''
        My Solution
        '''
        words = sentence.split()
        n = len(words)
        cur = 0
        while cur < n:
            if words[cur][-1] != words[(cur+1)%n][0]:
                return False
            cur += 1

        return True
        
