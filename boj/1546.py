N=int(input())
score=list(map(int,input().split()))

aver=(sum(score)*100)/(len(score)*max(score))

print(aver)
