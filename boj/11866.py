N,K=map(int,input().split())
circle=[i for i in range(1,N+1)]
result=[]

i=0

# while loop ver.
'''
while j!=0:
    result.append(circle[(i+K-1)%j])
    del circle[(i+K-1)%j]
    i=(i+K-1)%j
    j-=1
'''

# for loop ver.
for j in range(N,0,-1):
    result.append(circle[(i+K-1)%j])
    del circle[(i+K-1)%j]
    i=(i+K-1)%j
    
print('<',end='')
print(*result, sep=', ', end='')
print('>')
