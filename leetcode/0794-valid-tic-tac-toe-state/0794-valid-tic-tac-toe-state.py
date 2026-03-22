class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xc, oc = 0, 0
        # X와 O의 개수를 세서 같거나 X가 한개 더 많은지 확인
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    xc += 1
                elif board[i][j] == 'O':
                    oc += 1

        if xc - oc > 1 or xc < oc:
            return False

        # 빙고 위치 찾기
        x_bingo = []
        o_bingo = []

        # d = [(0, 1), (1, 1), (1, 0)]
        # 가로
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                pos = [i * 3, i * 3 + 1, i * 3 + 2]
                if board[i][0] == 'X':
                    x_bingo.append(pos)
                elif board[i][0] == 'O':
                    o_bingo.append(pos)
        
        # 세로
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                pos = [j, 3 + j, 6 + j]
                if board[0][j] == 'X':
                    x_bingo.append(pos)
                elif board[0][j] == 'O':
                    o_bingo.append(pos)
        
        # 대각선
        if board[0][0] == board[1][1] == board[2][2]:
            pos = [0, 4, 8]
            if board[0][0] == 'X':
                x_bingo.append(pos)
            elif board[0][0] == 'O':
                o_bingo.append(pos)

        if board[0][2] == board[1][1] == board[2][0]:
            pos = [2, 4, 6]
            if board[0][2] == 'X':
                x_bingo.append(pos)
            elif board[0][2] == 'O':
                o_bingo.append(pos)

        nx = len(x_bingo)
        no = len(o_bingo)
        # X와 O 둘다 빙고가 만들어졌는지 확인        
        if nx > 0 and no > 0:
            return False
        
        # X 빙고인데 개수가 같거나 O 빙고인데 X 개수가 큰 경우 False
        if (nx > 0 and (xc == oc)) or (no > 0 and (xc > oc)):
            return False

        return True
