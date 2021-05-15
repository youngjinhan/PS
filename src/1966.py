T=int(input())
for i in range(T):
    
    N,M=map(int,input().split())
    case=list(map(int,input().split()))

    j=0
    order=1
    while True:
        if case[j]==max(case):
            if j==M:
                print(order)
                break
            order+=1
            case[j]=0
        j=(j+1)%N
            

