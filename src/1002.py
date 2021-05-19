T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())

    r3=((x2-x1)**2+(y2-y1)**2)**0.5
    #print("r3:",r3)
    if r3==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2>r3:
            if abs(r1-r2)>r3:
                print(0)
            elif abs(r1-r2)==r3:
                print(1)
            else:
                print(2)
        elif r1+r2==r3:
            print(1)
        elif r1+r2<r3:
            print(0)
