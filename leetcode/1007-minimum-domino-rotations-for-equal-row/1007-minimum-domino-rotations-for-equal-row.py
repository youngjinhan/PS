class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        leng = len(tops)
        cand = set()
        cand.add(tops[0])
        cand.add(bottoms[0])

        for x, y in zip(tops, bottoms):
            if x not in cand and y not in cand:
                return -1

            cand = {c for c in cand if c == x or c == y}
        
        ans = inf
        for c in cand:
            top_cnt, bot_cnt = 0, 0
            for i in range(leng):
                if tops[i] != c:
                    top_cnt +=1
                elif bottoms[i] != c:
                    bot_cnt +=1

            ans = min(min(min(top_cnt, leng - top_cnt), min(bot_cnt, leng - bot_cnt)), ans)
        
        return ans
            
          