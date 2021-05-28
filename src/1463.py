N=int(input())
count=[[] for _ in range(N+1)]
count[1]=0
#print(count)

for i in range(2,N+1):
    if i%6==0:
        if count[i//3]>count[i//2]:
            count[i]=count[i//2]+1
        else:
            count[i]=count[i//3]+1
        if count[i]-1>count[i-1]:
            count[i]=count[i-1]+1
    elif i%3==0:
        if count[i//3]>count[i-1]:
            count[i]=count[i-1]+1
        else:
            count[i]=count[i//3]+1
    elif i%2==0:
        if count[i//2]>count[i-1]:
            count[i]=count[i-1]+1
        else:
            count[i]=count[i//2]+1
    else:
        count[i]=count[i-1]+1

print(count[N])
