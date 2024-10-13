from collections import deque

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        arr_order = sorted([i for i in range(n)], key = lambda x: (times[x][0]))
        leave_order = sorted([i for i in range(n)], key = lambda x: (times[x][1], x))
        seats = [None] * n
        seated_num = [None] * n
        min_empty_num = 0

        arr_cur, leave_cur = 0, 0
        leave_time = times[leave_order[leave_cur]][1]


        while arr_cur < n:
            arr_time = times[arr_order[arr_cur]][0]
            while leave_cur < n and leave_time <= arr_time:
                seat_no = seated_num[leave_order[leave_cur]]
                min_empty_num = min(min_empty_num, seat_no)
                seats[seat_no] = None
                seated_num[leave_order[leave_cur]] = None

                leave_cur += 1
                leave_time = times[leave_order[leave_cur]][1]
            
            if arr_order[arr_cur] == targetFriend:
                return min_empty_num

            seats[min_empty_num] = arr_order[arr_cur]
            seated_num[arr_order[arr_cur]] = min_empty_num
            arr_cur += 1

            while min_empty_num < n and seats[min_empty_num] != None:
                min_empty_num += 1