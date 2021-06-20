T=int(input())

for i in range(T):
    a,b=map(int,input().split())
    result=a**(b%4+4)%10
    if result:
        print(result)
    else:
        print(10)
