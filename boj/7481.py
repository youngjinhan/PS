t=int(input())
for i in range(t):
    a,b,S=map(int,input().split())
    if a>b:
        big=a
        small=b
    else:
        big=b
        small=a
    A=S//big
    s=S%big
    B=0
    if s%small==0:
        B=s//small
    else:
        while A>0:
            A-=1
            s+=big
            if s%small==0:
                B=s//small
                break
    if A==0 and B==0:
        print("Impossible")
    else:
        if a>b:
            print(A,B)
        else:
            print(B,A)

