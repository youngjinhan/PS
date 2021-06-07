digit=[list(input().split()) for _ in range(5)]
tmp=[] # 하나의 6자리수를 넣기 위한 공간
answer=[] # 중복되지 않는 6자리의 수들 저장 공간

def dfs(a,b):
    #print(a,b)
    global tmp
    #print(tmp)
    if len(tmp)==6:
        string=''.join(tmp)
        if string not in answer:
            answer.append(string)
        return

    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    for i in range(4):
        x=a+dx[i]
        y=b+dy[i]
        if x<0 or x>=5 or y<0 or y>=5:
            continue
        tmp.append(digit[x][y])
        dfs(x,y)
        del tmp[-1]
       

for i in range(5):
    for j in range(5):
        tmp=[digit[i][j]]
        dfs(i,j)
#print(answer)
print(len(answer))

