class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        p = set()
        ans = 0
        self_pal = False
        for word in words:
            if word[0] == word[1]:
                self_pal = True
            if word[::-1] in p:
                p.remove(word[::-1])
                ans += 4
                continue
            p.add(word)
        if self_pal:
            ans += 2
        return ans