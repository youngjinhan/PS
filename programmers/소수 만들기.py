from itertools import combinations
import math
def solution(nums):
    answer = 0
    
    coms=list(combinations(nums,3))
    for com in coms:
        num=sum(com)
        if isPrime(num):
            answer+=1
    return answer

def isPrime(a):
    if(a<2):
        return False
    for i in range(2,math.floor(pow(a,1/2))+1):
        if(a%i==0):
            return False
    return True
