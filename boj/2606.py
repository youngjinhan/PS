N=int(input())
E=int(input())
edge=[list(map(int,input().split())) for i in range(E)]

connect=[1]

added=1

while added:
    added=0
    for i in range(E):
        x,y=edge[i]
        for j in range(len(connect)):
            if x==connect[j]:
                if y not in connect:
                    connect.append(y)
                    added=1
            elif y==connect[j]:
                if x not in connect:
                    connect.append(x)
                    added=1

print(len(connect)-1)
