N=int(input())
ppl=list(map(int,input().split()))
pos=[]

for i in range(-1,-N-1,-1):
    pos.insert(ppl[i],N+i+1)

for i in pos:
    print(i, end=' ')
