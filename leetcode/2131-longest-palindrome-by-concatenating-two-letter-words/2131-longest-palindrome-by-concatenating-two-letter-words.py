class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        words_cnt = defaultdict(int)
        for word in words:
            rev = word[::-1]
            if words_cnt[rev] > 0:
                words_cnt[rev] -= 1
                ans += 4
                continue
            words_cnt[word] += 1

        for w in words_cnt:
            if words_cnt[w] > 0 and w[0] == w[1]:
                ans += 2
                break
    
        return ans