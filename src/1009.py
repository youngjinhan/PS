T=int(input())

for i in range(T):
    a,b=map(int,input().split())
    result=((a%10)**(b%4+4))%10
    if result==0:
        print(10)
    else:
        print(result)
