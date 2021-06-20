N,M=map(int,input().split())

space=[list(map(int, input().split())) for _ in range(N)]
shark=[]
max_safe=0

for i in range(N):
    for j in range(M):
        if space[i][j]==1:
            shark.append([i,j])

for i in range(N):
    for j in range(M):
        if space[i][j]==1:
            continue
        leng=0
        local_safe=N+M
        for x,y in shark:
            tmp_x=x
            tmp_y=y
            #print("i,j:",i,j,"x,y:",x,y)
            while i!=tmp_x and j!=tmp_y:                
                if i>tmp_x:
                    dx=1
                else:
                    dx=-1
                if j>tmp_y:
                    dy=1
                else:
                    dy=-1
                tmp_x+=dx
                tmp_y+=dy
                
                leng+=1
            #print("i,j:",i,j,"tmp_x,tmp_y:",tmp_x,tmp_y)
            if i!=tmp_x:
                leng+=abs(i-tmp_x)
            else:
                leng+=abs(j-tmp_y)
            #print("leng:",leng)
            if leng<local_safe:
                local_safe=leng
            #print("local safe leng:",local_safe)
            leng=0
        if local_safe>max_safe:
            max_safe=local_safe
        #print("max safe:" ,max_safe)
                
                

print(max_safe)
            

