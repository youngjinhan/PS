K,N=map(int,input().split())
line=[]
for i in range(K):
    line.append(int(input()))

line.sort()

right=line[-1]
left=1
mid=(left+right)//2

while left<=right:
    
    #print(left,right,mid)
    count=0
    for j in range(K):
        count+=line[j]//mid
    if count<N:  # right를 줄여야함
        right=mid-1
    else:
        ans=mid
        left=mid+1
    mid=(left+right)//2

print(ans)
