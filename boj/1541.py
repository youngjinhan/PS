form=input()

cur=0
flag=0
result=0
new_n_flag=0
num=0
while cur<len(form):
    if form[cur]=='-':
        if flag:
            result-=num
        else:
            result+=num
        if not flag:
            flag+=1
        new_n_flag=1
        

    elif form[cur] =='+':
        new_n_flag=1
        if flag:
            result-=num
        else:
            result+=num
        
    else:
        if new_n_flag:
            new_n_flag-=1
            num=int(form[cur])
        else:
            num=num*10+int(form[cur])

        if cur==len(form)-1:
            if flag:
                result-=num
            else:
                result+=num

    cur+=1
print(result)
