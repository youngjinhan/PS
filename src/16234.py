import sys
sys.setrecursionlimit(5000)
def color(pop,i,j):
    for k in range(4):
        x=i+dx[k]
        y=j+dy[k]
        if x<0 or x>=N or y<0 or y>=N:
                    continue
        #print("i,j",i,j,"  x,y:",x,y, "unity_count:",unity_count)
        if abs(pop[i][j]-pop[x][y])>=L and abs(pop[i][j]-pop[x][y])<=R:
            if unity[i][j]==0:
                #print(i,j,"colored")
                unity[i][j]=unity_count
            if unity[x][y]!=unity_count:
                #print(x,y,"colored")
                unity[x][y]=unity_count
                #print("recursion")
                color(pop,x,y)
                    
        

N,L,R=map(int,input().split())

pop=[list(map(int, input().split())) for _ in range(N)]
unity=[[0 for col in range(N)] for row in range(N)]
#print(unity)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

unity_count=1
unity_sum=0
move_count=0

while True:
    for i in range(N):
        for j in range(N):
            
            if unity[i][j]==0:
                color(pop,i,j)
                if unity[i][j]!=0:
                    #print("연합 생성")
                    unity_count+=1
                    #print(unity)
                
    #print(unity_count)
    #print(unity)
    if unity_count==1:
        break
    
    #print(moved_pop)
    k=1
    count=0
    while k<unity_count:
        for i in range(N):
            for j in range(N):
                if unity[i][j]==k:
                    unity_sum+=pop[i][j]
                    count+=1
        moved_pop=int(unity_sum/count)
        #print("이동후 영역당 인구수",moved_pop)
        for i in range(N):
            for j in range(N):
                if unity[i][j]==k:
                    pop[i][j]=moved_pop
                    unity[i][j]=0
        unity_sum=count=0
        k+=1
        
    
    unity_count=1
    #print(unity)
    #print(pop)

    move_count+=1

print(move_count)
