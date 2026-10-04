class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        info = []
        num = 0

        for trip in trips:
            n, start, end = trip
            info.append((start, n))
            info.append((end, -n))

        info.sort()

        for i in info:
            num += i[1]
            if num > capacity:
                return False
        return True