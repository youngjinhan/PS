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

# stay the length of original input list
# time complexity is worst of the 3 ways
'''
cur=0
while len(result)<N:
    if circle[i]!=0:
        cur+=1
        if cur==K:
            result.append(circle[i])
            circle[i]=0
            cur=0
    i=(i+1)%N
'''

print('<',end='')
print(*result, sep=', ', end='')
print('>')


