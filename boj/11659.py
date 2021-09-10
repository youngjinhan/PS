import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
nums=list(map(int,input().rstrip().split()))

result=[0 for _ in range(N+1)]
for i in range(N):
    result[i+1]=result[i]+nums[i]
    
for _ in range(M):
    i,j=map(int,input().rstrip().split())
    print(result[j]-result[i-1])
