class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MAX_MINS = 24 * 60
        def timeToInt(time):
            h, m = map(int, time.split(":"))
            return h * 60 + m


        time_list = [timeToInt(time) for time in sorted(timePoints)]
        n = len(timePoints)
        ans = MAX_MINS

        for i in range(n):
            gap = (time_list[(i + 1) % n] - time_list[i]) % MAX_MINS
            if gap == 0:
                return gap
            ans = min(ans, gap)

        return ans