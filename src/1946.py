import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    cnd=[[] for i in range(N+1)]
    for i in range(N):
        rsme, intv=map(int,input().split())
        cnd[rsme]=intv

    cnt=1
    criteria=cnd[1] # 면접 합격기준. 이 등수보다 순위가 높아야함.
    for i in range(2,N+1):
        if cnd[i]<criteria:
            criteria=cnd[i]
            cnt+=1

    print(cnt)
