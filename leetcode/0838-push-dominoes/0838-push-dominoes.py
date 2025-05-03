class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        leng = len(dominoes)
        MIN = -10**5
        r_arr = [MIN] * leng
        l_arr = [MIN] * leng
        ans = [None] * leng
        
        n = MIN
        for i in range(leng):
            if dominoes[i] == 'R':
                n = 0
            elif dominoes[i] == 'L':
                n = MIN
            r_arr[i] = max(n, r_arr[i])
            n -= 1
        
        m = MIN
        for i in range(leng-1, -1, -1):
            if dominoes[i] == 'L':
                m = 0
            elif dominoes[i] == 'R':
                m = MIN
            l_arr[i] = max(m, l_arr[i])
            m -= 1

        print(r_arr, l_arr)
        
        for i in range(leng):
            if r_arr[i] > l_arr[i]:
                ans[i] = 'R'
            elif r_arr[i] < l_arr[i]:
                ans[i] = 'L'
            else:
                ans[i] = '.'
        return "".join(ans)


        # '''
        # 처음부터 순회하면서 R이 나오면 거기부터 시작지점으로 끊음
        # L이 나오면 거기서 종료지점으로 끊음.
        # ..이 나오면 그냥 쭉
        # ..이 나오다 L이 나오면 다 L
        # ..이 나오다 R이 나오면 거기서 시작
        # R로 가다가 R이 나오면 그 사이 다 R로 채워넣음
        # R로 가다가 L이 나오면 그 사이 비교해서 넣기
        # L로 가면 거기서 끊고 다시 다음꺼부터 시작

        # '''
        # ans = []
        # length = len(dominoes)

        # cur = 0
        # start = 0
        # start_c = dominoes[cur]
        # while cur < length:
            
        #     print("cur =", cur, "c=",dominoes[cur])
        #     if dominoes[cur] == 'R':
        #         if start_c == '.':
        #             ans.append('.' * (cur - start))
        #             start_c = 'R'
        #             print(1)
        #         elif start_c == 'R':
        #             ans.append('R' * (cur - start))
        #             print(2)
        #         else:
        #             start_c = 'R'
        #         start = cur

        #     elif dominoes[cur] == '.' and start_c == 'L':
        #             start_c = '.'
        #             start = cur
        #             print(3)
        #     elif dominoes[cur] == 'L':
        #         if start_c == '.':
        #             ans.append('L' * (cur - start + 1))
        #             start_c = 'L'
        #             start = cur
        #             print(4)
        #         elif start_c == 'L':
        #             ans.append('L')
        #             start = cur
        #             print(5)
        #         else:
        #             part_leng = cur - start + 1
        #             # print(part_leng)
        #             ans.append('R' * (part_leng // 2) + '.' * (part_leng % 2) + 'L' * (part_leng // 2))
        #             start_c = 'L'
        #             start = cur
        #             print(6)
        #     cur += 1
        # if start_c == 'R' or start_c == '.':
        #     ans.append(start_c * (cur - start))
        # return "".join(ans)

                
                

        
        