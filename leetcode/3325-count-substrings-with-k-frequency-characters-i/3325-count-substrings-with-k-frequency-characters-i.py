class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        '''
        sliding window solution(hard to understand)
        eliminate values that don't meet the condition
        '''
        n = len(s)
        res = (n + 1) * n // 2
        count = Counter()
        i = 0
        for j in range(n):
            count[s[j]] += 1
            while count[s[j]] >= k:
                count[s[i]] -= 1
                i += 1
            res -= j - i + 1
        return res


        '''
        '''
        n = len(s)
        result = 0
        for i in range(n):
            freq = [0] * 26
            num_at_least_k = 0
            for j in range(i, n):
                index = ord(s[j]) - ord('a')
                freq[index] += 1
                if freq[index] == k:
                    num_at_least_k += 1
                # 추가로 freq[index]가 k를 초과했어도 num_at_least_k는 그대로 유지
                if num_at_least_k > 0:
                    result += 1
        return result