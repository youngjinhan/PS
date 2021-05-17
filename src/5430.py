
T=int(input())
for i in range(T):
    p=list(input())
    n=int(input())
    if n>0:
        arr=list(map(int,input()[1:-1].split(',')))
    else:
        input()
        arr=[]
    #print(arr)
    try:
        j=R_num=0
        while j<len(p):
            #print("j,len(p):",j,len(p))
            while j<len(p) and p[j]=='R':
                j+=1
                R_num+=1
            #print("2. j,len(p):",j,len(p))
            if j==len(p):
                break
            #print("3. j,len(p):",j,len(p))
            if p[j]=='D':
                if R_num%2==1:
                    del arr[-1]
                    #print(arr)
                else:
                    del arr[0]
                    #print(arr)
            j+=1
        if len(arr)>0 and R_num%2==1:
            arr.reverse()
        '''
        if len(arr)==0:
            print("[]")
        else:
            for j in range(len(arr)):
                if j==0:
                    print("[", end='')
                if j!=len(arr)-1:
                    print(arr[j],end=',')
                else:
                    print(arr[j], end=']\n')
        '''
        arr=list(map(str,arr))
        print("["+','.join(arr)+']')
    except Exception as err:
        print("error")


