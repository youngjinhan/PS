from collections import defaultdict

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_loc = []
        n = len(s)
        neighbor_candle = [None] * n
        
        for i in range(n):
            if s[i] == '|':
                candle_loc.append(i)

        n_c = len(candle_loc)
        if n_c < 2:
            return [0] * len(queries)

        candle_idx = defaultdict(int)
        for i in range(n_c):
            candle_idx[candle_loc[i]] = i

        candle_pos = 0
        candle_left = -1
        candle_right = candle_loc[candle_pos]
        for i in range(n):
            if i < candle_right:
                neighbor_candle[i] = [candle_left, candle_right]
            elif i == candle_right:
                candle_left = candle_right
                neighbor_candle[i] = [candle_left, candle_right]
                candle_pos += 1
                candle_right = 10**6 if candle_pos >= n_c else candle_loc[candle_pos]
        
        # print(neighbor_candle)

        answer = []
        for q in queries:
            left, right = q
            cl, cr = neighbor_candle[left][1], neighbor_candle[right][0]

            cnt = 0 if cl > cr else cr - cl - (candle_idx[cr] - candle_idx[cl])
            answer.append(cnt)

        return answer