N,K=map(int,input().split())
circle=[i for i in range(1,N+1)]
eliminated=[]

i=0
j=N
while len(eliminated)<N:
    eliminated.append(circle[(i+K-1)%j])
    del circle[(i+K-1)%j]
    i=(i+K-1)%j
    j-=1
    
print('<',end='')
print(*eliminated, sep=', ', end='')
print('>')
