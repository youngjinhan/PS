T=int(input())
n=[int(input()) for _ in range(T)]

for i in n:
    digit=0
    while i>0:
        #print("i",i)
        if i%2==1:
           print(digit,end=' ')
        digit+=1
        i=int(i/2)
    print("")
