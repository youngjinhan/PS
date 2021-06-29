N = input()
A = set(input().split())
M = input()

for m in input().split():
    print(int(m in A))
    

'''
N = int(input())
A = set(map(int, input().split()))
M = int(input())

for m in map(int,input().split()):
    print(int(m in A))
'''



'''
N=int(input())
A=sorted(list(map(int,input().split())))
#print(A)
M=int(input())
B=list(map(int,input().split()))
for i in B:
    left=0
    right=N-1

    if A[left]==i or A[right]==i:
        print(1)
    else:
        exist=0
        while left<right:
            mid=round((left+right+0.1)/2)
            #print(left,mid,right)
            if A[mid]<i:
                left=mid
            elif A[mid]>i:
                right=mid-1
            else:
                exist=1
                break
        print(exist)
'''
