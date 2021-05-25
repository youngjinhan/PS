A,B=map(int,input().split())

loc=0 #처음부터 숫자가 바뀌는 구간을 경계로 위치를 체크해나가며 계산

i=0
while loc<A:
    i+=1
    loc+=i
   
result=(loc-(A-1))*i

while loc<B:
    i+=1
    loc+=i
    result+=i**2

result-=(loc-B)*i
    
print(result)
