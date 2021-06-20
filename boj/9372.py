#import sys
from sys import stdin
input=stdin.readline

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    
    for j in range(M):
        input()
    '''
    result=str(N-1)+'\n'
    sys.stdout.write(result)
    '''
    print(N-1)
