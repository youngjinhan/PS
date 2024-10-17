class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        right_max_list = [None] * n
        right_max_list[-1] = (num_str[-1], n-1)

        for i in range(n-2, -1, -1):
            right_max_list[i] = right_max_list[i+1] if num_str[i] <= right_max_list[i+1][0] else (num_str[i], i)
        
        for i in range(n):
            if num_str[i] < right_max_list[i][0]:
                num_str[i], num_str[right_max_list[i][1]] = right_max_list[i][0], num_str[i]
                break

        return int(''.join(num_str))

