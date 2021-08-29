T=int(input())
for _ in range(T):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    count=0
    for i in range(n):
        
        cx,cy,r=map(int,input().split())
        loc1=(cx-x1)**2+(cy-y1)**2>r**2
        loc2=(cx-x2)**2+(cy-y2)**2>r**2
        if loc1 != loc2:
            count+=1
    print(count)
