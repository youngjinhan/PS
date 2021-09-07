import sys
input=sys.stdin.readline

N,M=map(int,input().split())
dogam=['']
for i in range(N):
    dogam.append(input().rstrip())

for i in range(M):
    arg=input().rstrip()
    try:
        print(dogam[int(arg)])
    except:
        print(dogam.index(arg))
