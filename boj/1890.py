N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]

'''
count=0
def dfs(board,i,j):
    #print(i,j)
    if board[i][j]==0:
        global count
        count+=1
        return
    x=i+board[i][j]
    y=j+board[i][j]
    if x<N:
        dfs(board,x,j)
    if y<N:
        dfs(board,i,y)


dfs(board,0,0)
print(count)
'''

count=[[0 for col in range(N)] for row in range(N)]
i=N-1
j=N-2
count[i][j+1]=1
while True:
    tmp=0
    if j+board[i][j]<N:
        tmp+=count[i][j+board[i][j]]
    if i+board[i][j]<N:
        tmp+=count[i+board[i][j]][j]
    #print(i,j,tmp)
    count[i][j]= tmp
    if i==0:
        if j==0:
            break
        else:
            j-=1
    else:
        if j==0:
            j=N-1
            i-=1
        else:
            j-=1

print(count[0][0])
