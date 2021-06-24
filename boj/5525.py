import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
S=input()

io=0
cnt=0
result=0
for i in range(1,len(S)):
    if S[i-1]=='I' and S[i]=='O':
        io=1
    elif S[i-1]=='O' and S[i]=='I' and io:
        cnt+=1
        if cnt>=N:
            result+=1
    else:
        io=0
        cnt=0
    
print(result)
