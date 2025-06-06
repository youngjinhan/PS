class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        '''
        Set with Sorted Insertion
        Time Complexity: O(nlogn)
        '''
        times = sorted(
            [
                (arrival, leave, index)
                for index, (arrival, leave) in enumerate(times)
            ]
        )

        next_chair = 0
        available_chairs = []
        leaving_queue = []

        for time in times:
            arrival, leave, index = time

            # Free up chairs based on current time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_queue)
                heapq.heappush(available_chairs, chair)

            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                current_chair = next_chair
                next_chair += 1

            # Check if it's the target friend
            if index == targetFriend:
                return current_chair

            # Push current leave time and chair
            heapq.heappush(leaving_queue, (leave, current_chair))

        return 0

        '''
        Event-based with Two Priority Queues
        Time Complexity: O(nlogn)
        '''

        n = len(times)
        events = []
        for i in range(n):
            events.append([times[i][0], i])
            events.append([times[i][1], ~i])

        events.sort()

        available_seats = list(range(n))
        occupied_seats = []

        for event in events:
            time, friend = event
            while occupied_seats and occupied_seats[0][0] <= time:
                _, seat = heapq.heappop(occupied_seats)
                heapq.heappush(available_seats, seat)
            
            if friend >= 0:
                seat = heapq.heappop(available_seats)

                if friend == targetFriend:
                    return seat
                heapq.heappush(occupied_seats, [times[friend][1], seat])

        return -1  # should not come to this point


        '''
        My Solution
        Time Complexity: O(nlogn)
        '''
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