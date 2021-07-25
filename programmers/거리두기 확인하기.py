def check(m,n,depth):
    if depth==2:
        return 1
    # 시계방향순
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    is_good=1   # 상하좌우 모두 X일때, OX가 나오는 상황일 때
    for i in range(4):
        x=m+dx[i]
        y=n+dy[i]
        if x==5 or x<0 or y==5 or y<0 or visit[x][y]==1:
            continue

        if p[x][y]=='P':
            return 0
        elif p[x][y]=='O':
            is_good=check(x,y,depth+1)
        
            
    return is_good
            
def solution(places):
    answer = []

    for place in places:
        global p
        p=[]
        for i in place:
            p+=[list(i)]
        is_good=1
        for i in range(5):
            for j in range(5):
                if p[i][j]=='P':
                    global visit
                    visit=[[0 for col in range(5)] for row in range(5)]
                    visit[i][j]=1 # 코드짜기 번거로워서 처음시작 부분만 체크해줌. 처음 P는 다시 체크하면 결과에 영향을 주지만
                                  # 나중에 나오는 P는 한번 나올 시 즉시 0으로 리턴되므로 X나 O가 나올때 중복체크를 하지만
                                  # 결과에 영향을 주지 않음. 시간 복잡도가 중요한 문제면 방문여부 체크 해야함.
                    is_good=check(i,j,0)
                    if not is_good:
                        break
            if not is_good:
                break
        answer.append(is_good)
    return answer

places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
