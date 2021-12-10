n=int(input())

cnt=0
for i in range(n):
    check=[]
    string=input()
    allow=''
    leng=len(string)
    j=0
    group=1
    
    while j<leng:
        if string[j] not in check:
            allow=string[j]
            check.append(string[j])
        elif allow!=string[j]:
            group=0
            break
        j+=1
    if group:
        cnt+=1
print(cnt)
